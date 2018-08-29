#!/usr/bin/python3
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
import leseBuch
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

class BuecherLesen(object):

	def runLesen(self,dev=None, debug=False):
		#
		# This Function allows the user to chose a book to listen to.
		#
		# :param dev: the device that the input is coming from
		# :param debug: If debug messages are supposed to be printed
		#
		from teddy import getDevice, coutput, getButton, Notfall
		#
		self.vorlesen = leseBuch.LeseBuch()
		#
		self.debug=debug
		if dev is None:
			self.dev=getDevice(self.debug)
		else:
			self.dev=dev
		if self.debug:
			print("### Buecher Lesen mit debug output ....")
		if self.debug:
			print("### Bucher Lesen wurde gestartet ....")
		Lesen=True
		coutput("Choose a author")
		coutput("Press my left arm to select another")
		coutput("Press my right arm to select this")
		while Lesen:
			for author in os.listdir(teddy_books):
				while Lesen:
					if self.debug:
						print(">>>> %s" % author)
					coutput(author.replace("_"," "))
					pressed=getButton(self.dev, 5, self.debug)
					if pressed==RECHTER_ARM:
						if self.debug:
							print("### Starte %s" % author)
						coutput(author.replace("_"," "))
						coutput("was selected")
						coutput("Choose a book")
						coutput("Press my left arm to select another")
						coutput("Press my right arm to select this")
						while Lesen:
							for buch in os.listdir("%s%s" % (teddy_books,author)):
								if buch.endswith(".mp3"):
									if self.debug:
										print(">>>> %s" % buch)
									coutput(buch.replace("_"," ").replace(".mp3",""))
									pressed=getButton(self.dev, debug = self.debug)
									if pressed==RECHTER_ARM:
										if self.debug:
											print("### Starte %s" % buch)
										coutput(buch.replace("_"," ").replace(".mp3",""))
										coutput("was selected")
										self.vorlesen.runVorlesen(self.dev,buch.replace(".mp3",""),author, debug=self.debug)
										Lesen=False
										break

									elif pressed==LINKER_ARM:
										if self.debug:
											print("### Weiter")
									elif pressed==NOTFALL:
										Notfall()
										Lesen=False
									elif pressed==BEENDEN:
										if self.debug:
											print("### Bucher Lesen wird beendet")
										Lesen=False
										break
						break
					elif pressed==LINKER_ARM:
						if self.debug:
							print("### Weiter")
						break
					elif pressed==TIMEOUT:
						if self.debug:
							print("### Weiter")
						break
					elif pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						if self.debug:
							print("### Bucher Lesen wird beendet")
						Lesen=False
						break
					else:
						if self.debug:
							print("### noch nichts ...")

		if self.debug:
			print("### Beende Hoerbuecher")
		coutput("Book reading was closed")
