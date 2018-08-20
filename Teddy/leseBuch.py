#!/usr/bin/python2.7
# coding: utf8
#
# @author: Michael Wintersperger <mwintersperger@student.tgm.ac.at>, Simon Appel <sappel@student.tgm.ac.at>
# @version: 20180608
#
# @description: Teddy - the interactive Hedgehog teddy bear client
#
import sys
import signal
import random
import pygame
import time
import threading
import psycopg2
#
teddy_home="."
teddy_books="%s/books/" % teddy_home
import os
if os.path.exists("/home/pi"):
	teddy_home="/home/pi/Teddy/"
	teddy_books="/home/pi/Teddy/books/"
#
from espeak import espeak, core
#
RECHTER_ARM=1
LINKER_ARM=2
RECHTES_BEIN=3
LINKES_BEIN=4
BEENDEN=5
NOTFALL=6
TIMEOUT=7
LINE="--------------------------------------------------------------------"
#
import gettext

class LeseBuch(object):
	def runVorlesen(self,dev=None,name=None,author=None,genre=None,path=None,ausgewaehlt=False,pausiert=False,vorgelesen=0,debug=False):
		#
		# This Function is called when a user wants to have a book read to him or her.
		# It runs the audio file of the book, listens for interrupts and allows the usersto start from exiting bookmarks instead of the beginning of the book.
		#
		from teddy import getDevice, coutput, getButton, Notfall
		#
		self.debug=debug
		if self.debug:
			print("### Lese Buch mit debug output ....")
		if dev is None:
			self.dev=getDevice(self.debug)
		else:
			self.dev=dev
		self.overlap=3 # seconds overlap when re-reading
		self.name=name
		self.author=author
		if genre is not None:
			self.genre=genre
		else:
			self.genre="Maerchen"
		self.path=path
		self.ausgewaehlt=ausgewaehlt
		self.pausiert=pausiert
		self.vorgelesen=vorgelesen		
		if self.debug:
			print("### Vorlesen %s %s" % (self.author,self.name))

		if self.path is None:
			if self.author is None or self.name is None:
				if self.debug:
					print("### Sorry, weder author und name noch pfad angegeben")
				return 
			mp3=teddy_books+self.author.replace(" ","_").replace("ü","ue").replace("ß","ss").replace("ö","oe").replace("ä","ae")+"/"+self.name.replace(" ","_").replace("ü","ue").replace("ß","ss").replace("ö","oe").replace("ä","ae")+".mp3"
		else:
			mp3=self.path
		if self.debug:
			print("### %s" % mp3)
		vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, self.pausiert, self.vorgelesen)
		if os.path.exists(mp3):
			if self.vorgelesen == 0: # normal wenn nicht uebergeben
				self.vorgelesen=vorgelesen

			if self.debug:
				print("### %s wurde bereits vorgelesen %d seconds" % (mp3,self.vorgelesen))

			if self.vorgelesen > 0:
				coutput("Press my right arm to start from the Bookmark")
				coutput("Press my left arm to start from the beginning")
				Check=True
				while Check:
					pressed=getButton(self.dev, 10, self.debug)
					if pressed==BEENDEN:
						if self.debug:
							print("### Beenden")
						Check=False
						return
					elif pressed==NOTFALL:
						if self.debug:
							print("### Notfall")
						Notfall()
						Check=False
					elif pressed==LINKER_ARM:
						if self.debug:
							print("### Play %s from begin" % mp3)
						Check=False
						self.vorgelesen=0
					elif pressed==RECHTER_ARM:
						if self.debug:
							print("### Play %s after %d seconds" % (mp3,self.vorgelesen))
						Check=False
						# keep vorgelesen
					elif pressed==TIMEOUT:
						if self.debug:
							print("### Play %s from begin" % mp3)
						Check=False
						self.vorgelesen=0

			coutput("Press my right arm to pause reading")
			coutput("Press end to stop reading")

			start = int(time.time())
			print(">>>>>>>> Vorlesen %s at %d from %d" % (mp3,start,self.vorgelesen))

			pygame.mixer.music.load(mp3)
			pygame.mixer.music.play(1, self.vorgelesen-self.overlap)
#			pygame.mixer.Channel(0).play(pygame.mixer.Sound(mp3))

			Lesen=True
			Paused=False
			while pygame.mixer.music.get_busy() is not None and Lesen:
				pygame.time.Clock().tick(10)
				while Lesen:
					pressed=getButton(self.dev, 1, self.debug)
					if pressed==TIMEOUT and pygame.mixer.music.get_busy() is None:
						if self.debug:
							print("### Timeout")
					elif pressed==BEENDEN:
						now = int(time.time())
						lesezeit=now-start
						self.vorgelesen=self.vorgelesen+lesezeit
						if self.debug:
							print("### Beende %s after %d seconds" % (mp3,self.vorgelesen))

						vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, self.pausiert, self.vorgelesen)
						pygame.mixer.stop()
						Lesen=False
					elif pressed==NOTFALL:
						now = int(time.time())
						lesezeit=now-start
						self.vorgelesen=self.vorgelesen+lesezeit
						vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, Paused, self.vorgelesen)
						if self.debug:
							print("### Notfall %s" % mp3)
						Notfall()
						Lesen=False
					elif pressed==RECHTER_ARM:
						if not Paused:
							coutput("Reading paused")
							coutput("Press my right arm to resume reading")
							coutput("Press end to stop reading")
							now = int(time.time())
							lesezeit=now-start
							self.vorgelesen=self.vorgelesen+lesezeit
							vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, Paused, self.vorgelesen)
							if self.debug:
								print("### Paused %s after %d seconds" % (mp3,self.vorgelesen))

							pygame.mixer.stop()
							Paused=True
						else: # Paused
							coutput("Continuing reading")
							coutput("Press my right arm to pause reading")
							coutput("Press end to stop reading")
							Paused=False
							self.vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, Paused, 0)
							start = int(time.time())
							if self.debug:
								print("### Unpaused %s reading from %s" % (mp3,self.vorgelesen))
							pygame.mixer.music.load(mp3)
							pygame.mixer.music.play(1, self.vorgelesen-self.overlap)

		else:
			print("not found")
		pygame.mixer.music.stop()
		if self.debug:
			print("### Beendet %s after %d seconds" % (mp3,self.vorgelesen))
#		coutput("Hörbuecher hören wurde beendet")

	def updateBuch(self, name, author, genre, path, ausgewaehlt, pausiert, vorgelesen, debug=False):
#
#		insert a new gelesen value into the Buecher table
#
# 		Table Buch(
#     		name varchar(255) PRIMARY KEY,
#        	author varchar(255),
#        	genre varchar(20),
#        	path varchar(255)
#        	ausgewaehlt bool,
#        	pausiert bool,
#        	vorgelesen integer)
#
		nam=name.replace("_"," ")
		aut=author.replace("_"," ")
		if genre is not None:
			gen=genre.replace("_"," ")
		else:
			gen=""
		if ausgewaehlt:
			ausg="1"
		else:
			ausg="0"
		if pausiert:
			paus="1"
		else:
			paus="0"
		vorg=str(vorgelesen)


		select= """SELECT * FROM Buch WHERE name = %s;"""
		sql = """INSERT INTO Buch(name,author,genre,path,ausgewaehlt,pausiert,vorgelesen)
             VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING name;"""
		update = """UPDATE Buch set vorgelesen = %s WHERE name = %s;"""
		conn = None
		name_id = None
		try:
			conn = psycopg2.connect("dbname=teddy")
        		# create a new cursor
			cur = conn.cursor()
			cur.execute(select, ((nam,)))
			row = cur.fetchone()
			if row is not None:
				self.name=row[0]
				self.vorgelesen=int(row[6])
				if debug:
					print("### wurden bereits vorgelesen %d Sekunden" % (self.vorgelesen))
				if vorgelesen > 0 and self.vorgelesen != vorgelesen:
					print(">>>>>>>> updating name %s vorgelesen %d to %s" % (self.name,self.vorgelesen, vorg))
					cur.execute(update, (vorg,nam))
			else:
	        		# execute the INSERT statement
				cur.execute(sql, (nam,aut,gen,path,ausg,paus,"0"))
			        # get the generated id back
				name_id = cur.fetchone()[0]
			# commit the changes to the database
			conn.commit()
			# close communication with the database
			cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		finally:
			if conn is not None:
				conn.close()
		return self.vorgelesen
