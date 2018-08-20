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

class Termin(object):
	def __init__(self,dev=None,debug=False):
		#
		from teddy import getDevice, coutput
		#
		self.debug=debug
		if self.debug:
			print("### Termin mit debug output ....")
		if dev is None:
			self.dev=getDevice(self.debug)
		else:
			self.dev=dev

	def checkTermin(self, debug=False):
		#
		# This Function reads the Teddy DB.
		#
		conn = None
		epoch=0
		if True:
			#
			# Termine
			#
			conn = psycopg2.connect("dbname=teddy")
			cur = conn.cursor()
			cur.execute("SELECT * FROM Termine")
			row = cur.fetchone()
			while row is not None:
				self.name=row[0]
				self.datum=row[1]
				self.zeit=row[2]
				self.beschreibung=row[3]
				self.ort=row[4]
				self.hinweis=row[5]
				#
				# melde was gefunden wurde ...
				#
				self.meldeTermin()
				row = cur.fetchone()
			cur.close()
			cur = conn.cursor()
			#
			# Pillen
			#
			# get weekday:
			self.datum=datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) 
			weekday=datetime.today().weekday()

			cur.execute("SELECT * FROM Pillen")
			row = cur.fetchone()
			while row is not None:
				self.name=row[0]
				self.montag=row[1]
				self.dienstag=row[2]
				self.mittwoch=row[3]
				self.donnerstag=row[4]
				self.freitag=row[5]
				self.samstag=row[6]
				self.sonntag=row[7]
				self.anzahl=int(row[8])
				self.zeit=row[9]
				if self.montag and weekday==0:
					if debug:
						print("Pille am MONTAG")
					self.meldeTermin()
				if self.dienstag and weekday==1:
					if debug:
						print("Pille am DIENSTAG")
					self.meldeTermin()
				if self.mittwoch and weekday==2:
					if debug:
						print("Pille am MITTWOCH")
					self.meldeTermin()
				if self.donnerstag and weekday==3:
					if debug:
						print("Pille am DONNERSTAG")
					self.meldeTermin()
				if self.freitag and weekday==4:
					if debug:
						print("Pille am FREITAG")
					self.meldeTermin()
				if self.samstag and weekday==5:
					if debug:
						print("Pille am SAMSTAG")
					self.meldeTermin()
				if self.sonntag and weekday==6:
					if debug:
						print("Pille am SONNTAG")
					self.meldeTermin()
				self.beschreibung=""
				self.ort=""
				self.hinweis=""
				if debug:
					print("PILLE: ", self.name,self.montag,self.dienstag,self.mittwoch,self.donnerstag,self.freitag,self.samstag,self.sonntag,self.anzahl,self.zeit)
			row = cur.fetchone()
			cur.close()
			if conn is not None:
				conn.close()
		else:
			#
			# melde was uebergeben wurde ...
			#
			self.meldeTermin(debug)

	def meldeTermin(self, debug=False):
		#
		# This Function  checks if any date is set to the current time.
		#
		seconds = (self.zeit.hour * 60 + self.zeit.minute) * 60 + self.zeit.second
		epoch=time.mktime(self.datum.timetuple())+seconds
		te = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
		now = int(time.time())
		tn = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
		if debug:
			print("epoch %d (%s) now %d (%s)" % (epoch, te, now, tn))
		# schlimmstenfalls wird Termin 2x angesagt
		if epoch >= (now-30) and epoch < (now+30): 
			coutput("Termin")
			coutput(self.name)
			coutput("at")
			coutput(str(self.zeit.hour))
			coutput("hours")
			coutput(str(self.zeit.minute))
			coutput("minutes")
			if len(self.beschreibung) > 0:
				coutput("description")
				coutput(self.beschreibung)
			if len(self.ort) > 0:
				coutput("location")
				coutput(self.ort)
			if len(self.hinweis) > 0:
				coutput("hint")
				coutput(self.hinweis)
		else:
			if debug:
				print("Termin: ", self.name, self.datum, self.zeit, self.beschreibung, self.ort, self.hinweis)
				print("Schade, Termin ist nicht jetzt")
