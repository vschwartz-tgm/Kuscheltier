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
import os
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

class SimonSagt(object):
	def runSpiel(self, dev=None, task=None, debug=False):
		#
		# This function allows the user to play Simon Says.
		#
		from teddy import getDevice, coutput, getButton, Notfall
		#
		if dev is None:
			self.dev=getDevice(True)
		else:
			self.dev=dev
		self.task=task
		self.debug=debug
		if self.debug:
			print("### Simon Sagt mit debug output ....")
		self.name="Simon Sagt"
		if self.debug:
			print("### Simon sagt wurde gestartet ....")
		coutput("The Rules of Simon Says are as follows")
		coutput("When i say, Simon Says, then you must follow my orders")
		coutput("When i don't say Simon Says, then you must do nothing")
		self.punkte=0
		while True:
			print(">>>> PUNKTE: %d" % self.punkte)
			# ob Simon sagt ...
			zahl = random.randrange(1,100)
			if self.debug:
				print("### Zahl %d" % zahl)
			# welcher Körperteil ...
			limb = random.randrange(1,100)
			if self.debug:
				print("### Limb %d" % limb)
			if zahl < 50:
				coutput("Simon Says")
				if limb >= 1 and limb < 25:
					coutput("press my right arm")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==RECHTER_ARM:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 25 and limb < 50:
					coutput("press my left arm")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==LINKER_ARM:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 50 and limb < 75:
					coutput("press my right foot")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==RECHTES_BEIN:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 75 and limb < 100:
					coutput("press my left foot")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==LINKES_BEIN:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
			else:	# NO Simon says
				if limb >= 1 and limb < 25:
					coutput("press my right arm")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 25 and limb < 50:
					coutput("press my left arm")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 50 and limb < 75:
					coutput("press my right foot")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall(self.voice)
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
				elif limb >= 75 and limb < 100:
					coutput("press my left foot")
					pressed=getButton(self.dev, debug = self.debug)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Right")
						self.punkte+=1
					else:
						coutput("Wrong")
						self.punkte-=1
		if self.debug:
			print("Beende Simon Sagt")
		coutput("Simon Says was closed")
		print(">>>> FINALE PUNKTE: %i" % self.punkte)
		self.updateSpiel(self.name, self.punkte, self.debug)

		coutput("you have")
		coutput(str(self.punkte))
		coutput("points")

		if self.hoechststand < self.punkte:
			coutput("new highscore")
		else:
			coutput("Highscore")
			coutput(str(self.hoechststand))
			coutput("points")


	def updateSpiel(self, name, punkte, debug = False):
		#
		# This Function writes a new Highscore into the DB.
		#

		# insert a new gelesen value into the Spiele table
		#
		# Table Spiele(
		# name varchar(255) PRIMARY KEY,
		# punkte integer)
		#
		
		self.debug=debug
		self.name=name.replace("_"," ")
		self.punkte=str(punkte)
		self.hoechststand=0

		select= """SELECT * FROM Spiele WHERE name = %s;"""
		sql = """INSERT INTO Spiele(name,punkte) VALUES(%s,%s) RETURNING name;"""
		update = """UPDATE Spiele set punkte = %s WHERE name = %s;"""
		conn = None
		name_id = None
		try:
			conn = psycopg2.connect("dbname=teddy")
			# create a new cursor
			cur = conn.cursor()
			cur.execute(select, (self.name))
			row = cur.fetchone()
			if row is not None:
				self.hoechststand=int(row[1])
				if self.debug:
					print("### hoechststand %d Punkte %d" % (self.hoechststand, self.punkte))
				if self.punkte > 0 and self.hoechststand < self.punkte:
					print(">>>>>>>> updating name %s hoechststand %d to %s" % (self.name,self.hoechststand, self.punkte))
					cur.execute(update, (self.punkte,self.name))
			else:
				# execute the INSERT statement
				cur.execute(sql, (self.name,self.punkte))
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
