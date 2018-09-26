#!/usr/bin/python3
# -*- coding: utf-8 -*-
# coding: utf8
#
# @author: Michael Wintersperger <mwintersperger@student.tgm.ac.at>, Simon Appel <sappel@student.tgm.ac.at>
# @version: 20182008
#
# @description: Teddy - the interactive Hedgehog teddy bear client
#
teddy_version="0.19"
#
from evdev import InputDevice, categorize, ecodes
from select import select
#
import sys
import signal
import random
import pygame
import time
#
import os
#
from espeak import espeak, core
from datetime import datetime
#
from simonSagt import SimonSagt as SimonSagt
from buecherLesen import BuecherLesen as BuecherLesen
from power import Power as Power
from termin import Termin as Termin
#

teddy_home="."
teddy_books="%s/books/" % teddy_home
import os
if os.path.exists("/home/pi"):
	teddy_home="/home/pi/Teddy/"
	teddy_books="/home/pi/Teddy/books/"
	teddy_audio="/home/pi/Teddy/AudioFiles"

RECHTER_ARM=1
LINKER_ARM=2
RECHTES_BEIN=3
LINKES_BEIN=4
BEENDEN=5
NOTFALL=6
TIMEOUT=7
LINE="--------------------------------------------------------------------"
#
# currently unused sound parameters
#
amplitude=100
word_gap=10
capitals=1
line_length=1
pitch=50
speed=100
spell_punctuation=[]
#
import gettext
global teddy_language
teddy_language = "de"

from threading import Timer
from functools import partial

class IntervalTermin(object):
        def __init__(self, interval, function, args=[], kwargs={}):
            self.interval = interval
            self.function = partial(function, *args, **kwargs)
            self.running  = False
            self._timer   = None

        def __call__(self):
            self.running = False  # mark not running
            self.start()          # reset the timer for the next go
            self.function()       # call the partial function

        def start(self):
            if self.running:
                # Don't start if we're running!
                return
            # Create the timer object, start and set state.
            self._timer = Timer(self.interval, self)
            self._timer.start()
            self.running = True

        def stop(self):
            if self._timer:
                self._timer.cancel()
                self.running = False
                self._timer  = None

class IntervalPower(object):
        def __init__(self, interval, function, args=[], kwargs={}):
            self.interval = interval
            self.function = partial(function, *args, **kwargs)
            self.running  = False
            self._timer   = None

        def __call__(self):
            self.running = False  # mark not running
            self.start()          # reset the timer for the next go
            self.function()       # call the partial function
        def start(self):
            if self.running:
                # Don't start if we're running!
                return
            # Create the timer object, start and set state.
            self._timer = Timer(self.interval, self)
            self._timer.start()
            self.running = True

        def stop(self):
            if self._timer:
                self._timer.cancel()
                self.running = False
                self._timer  = None

def wait4pygame():
	#
	# A Function that checks if pygame is currently busy (with reading a book) every 10 ms
	#
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)

def wait4espeak(r):
	#
	# A Function that puts the programm to sleep while espeak is busy
	#
	# :param r: the synthesized text
	#
	done_synth = [False]
	def cb(event, pos, length):
		if event == espeak.core.event_MSG_TERMINATED:
			done_synth[0] = True
	espeak.set_SynthCallback(cb)
	while r and not done_synth[0]:
		time.sleep(0.10)

def coutput(text, debug=False):
	#
	# This function turn text into synthesized speech
	#
	# :param text: The text that is to be turned into speech
	# :param debug: If debug messages are supposed to be printed
	#
	print(">>>>>>>> %s" % text)
	global teddy_language
	langs = []
	langs.append(teddy_language)
	lg = gettext.translation('teddy', localedir='./locale', languages=langs)
	lg.install()
	espeak.core.set_voice(teddy_language)
	print(">>>>>>>> %s" % _(text))
	r=espeak.synth("   %s" % _(text))
	wait4espeak(r)

def getDevice(debug=False):
	#
	# A Function to detect suitable input devices
	#
	# :param debug: If debug messages are supposed to be printed
	#
	# :return: the device
	#
	inputs=open("/proc/bus/input/devices","r")
	line=inputs.readline()
	dv="none"
	while line:
		if line.find("Joystick") is not -1 or line.find("MOSIC      SPEED-LINK Competition Pro") is not -1:
			line=inputs.readline()
			line=inputs.readline()
			line=inputs.readline()
			line=inputs.readline()
			sp=[]
			sp=line.split()
			dv=sp[1].replace("Handlers=","")
			if dv.startswith("js"):
				dv=sp[2]
		line=inputs.readline()
	inputs.close()
	device="/dev/input/%s" % dv
	if os.path.exists(device):
		dev = InputDevice(device)
	else:
		if debug:
			print("         Input Device not available")
			print (LINE)
		return None
	device=str(dev)
	sp=[]
	sp=device.split(",")
	if debug:
		print("         Device:  %s" % sp[0].replace("device","").lstrip().rstrip())
		print("         Name:    %s" % sp[1].replace("name","").replace("\"","").lstrip().rstrip())
		print (LINE)
	return dev

def getButton(dev, timeout=5, debug=True):
	#
	# This Function listens for input and returns a enumeration depending on input
	#
	# :param dev: The device this function is supposed to listen to
	# :param timeout: How many seconds to wait for input
	# :param debug: If debug messages are supposed to be printed
	#
	# :return: Enumeration depending on input
	#
	if dev is None:
		dev=getDevice(debug)
	Running=True
	now = int(time.time())
	end=int(now+timeout)
	if debug:
		print(" Timeout %d ### now %d end %d" % (timeout, now,end))
	while now < end:
		if debug:
			print("### now %d" % now)
		now = int(time.time())
		event=dev.read_one()
		if event is not None:
			if event.type == 3 and event.code == 1 and event.value == 255:
				if debug:
					print("### Rechter Arm")
				return RECHTER_ARM
			elif event.type == 3 and event.code == 1 and event.value == 0:
				if debug:
					print("### Linker Arm")
				return LINKER_ARM
			elif event.type == 3 and event.code == 0 and event.value == 255:
				if debug:
					print("### Rechtes Bein")
				return RECHTES_BEIN
			elif event.type == 3 and event.code == 0 and event.value == 0:
				if debug:
					print("### Linkes Bein")
				return LINKES_BEIN
			elif event.type == 1 and event.code == 288 and event.value == 1:
				if debug:
					print("### Beenden")
				return BEENDEN
			elif event.type == 1 and event.code == 305 and event.value == 1:
				if debug:
					print("### Beenden")
				return BEENDEN
			elif event.type == 1 and event.code == 304 and event.value == 1:
				if debug:
					print("### Notfall")
				return NOTFALL
			elif event.type == 1 and event.code == 289 and event.value == 1:
				if debug:
					print("### Notfall")
				return NOTFALL
			else:
				if debug:
					pass
					# print(categorize(event))
					# print("### Type %s Code %s Value %s" % (event.type,event.code,event.value))
		now = int(time.time())
	#
	# while has ended due to timeout ...
	#
	if debug:
		print("### Timeout")
	return TIMEOUT

class Notfall(object):
	def __init__(self,voice):
		#
		# im Moment machen wir noch nicht viel ....
		#
		coutput("Emergency Eemergency Emergency")


class Teddy(object):
	def __init__(self, device=None, task=None, debug=False):
		self.debug=debug
		if self.debug:
			print("### Teddy mit debug output ....")
		self.task=task
		self.repeat=0
		#
		# init pygame for sound
		#
		# good sound parameters for raspi
		# maybe get later from config file or database
		#
		frequency=48000
		size=-16
		channels=1
		buffer=1024
		speed=100
		voice='de'
		#
		if pygame.mixer.get_init() is None:
			pygame.mixer.init(frequency, size, channels, buffer)
		#
		signal.signal(signal.SIGINT, signal_handler)
		#
		# init button device
		#
		if device is None:
			self.dev=getDevice(self.debug)
		else:
			self.dev=device
		#
		# initializing external classes
		#
		self.simon = SimonSagt()
		self.buecher = BuecherLesen()
		self.termine = Termin()
		self.power = Power()

		# call checkPower every 10 seconds, forever
		pt=IntervalPower(10.0, self.power.checkPower)
		pt.start()
		# call checkTermin every 30 seconds, forever
		rt=IntervalTermin(30.0, self.termine.checkTermin)
		rt.start()

		#
		# Choose a language
		#


        pygame.display.set_mode((200, 100))
        #pygame.mixer.music.load('D:\Diplomarbeit\Github\Kuscheltier\Teddy\Einleitung_Hallo2.wav')
        pygame.mixer.music.load("teddy_audio/Einleitung/Einleitung_Hallo.wav")
        pygame.mixer.music.play(0)

        clock = pygame.time.Clock()
        clock.tick(10)


		#pygame.mixer.music.play(1, 0)


		global teddy_language
		coutput("Choose your language, press the right arm for german and the left arm for english")
		pressed=getButton(self.dev, 10, self.debug)
		if pressed==RECHTER_ARM:
			teddy_language = "de"
		elif pressed==LINKER_ARM:
			teddy_language = "en"
		#
		# start task directly is defined for debugging ...
		#
		if self.task=="simon":
			self.simon.runSpiel(self.dev, self.debug)
		elif self.task=="buecher":
			self.buecher.runLesen(self.dev, self.debug)
		else:
			self.betterAsk(self.debug)

	def betterAsk(self, debug=False):
		#
		# This Function presents the user the available functions and allows said user to chose which one he or she wants to use.
		#
		# :param debug: If debug messages are supposed to be printed
		#
		Laufen=True
		while Laufen:
			if self.repeat < 5: # don't ask forever ...
				coutput("If you want to play Simon Says, press the right arm")
				coutput("If you want to listen to a book, press the left arm")
				coutput("If you want to turn me off, press the end button")
				self.repeat+=1
			pressed=getButton(self.dev, 10, debug)
			if pressed==RECHTER_ARM:
				self.repeat=0
				if debug:
					print("### Starte Simon Sagt")
				coutput("You choose to play Simon Says")
				self.simon.runSpiel(self.dev, self.debug)
				self.repeat=0
			elif pressed==LINKER_ARM:
				self.repeat=0
				if debug:
					print("### Starte Bücher Lesen")
				coutput("You choose to listen to books")
				self.buecher.runLesen(self.dev, self.debug)
				self.repeat=0
			elif pressed==NOTFALL:
				self.repeat=0
				if debug:
					print("### Notfall")
				Notfall(self.voice)
				self.repeat=0
			elif pressed==BEENDEN:
				self.repeat=0
				if debug:
					print("### Beenden")
				Laufen=False
				self.repeat=0
			else:
				# TIMEOUT or not (yet) used button ...
				if debug:
					print("### noch nichts ...")
		if debug:
			print("### Teddy wurde beendet")
		coutput("Teddy is shutting down")
		os._exit(0)

def signal_handler(signal, frame):
	#
	# This Function creates a clean exit for the Programm in case of crashes.
	#
	print("\n")
	coutput("Teddy is shutting down")
	os._exit(0)

def main():
	print (LINE)
	print ("                   >>>>>>>>>> Teddy V%s <<<<<<<<<<<" % teddy_version)
	print (LINE)
	debug=False
	task="none"

	power_check=True
	termin_check=True
	argv=sys.argv
	argc=len(sys.argv)
	for i in range(1,argc):
		if argv[i].startswith("-d"):
			debug=True
			print("         Debugging output ....")
			print (LINE)
		if argv[i].startswith("-s"):
			print("         direkt Simon Says ....")
			task="simon"
			print (LINE)
		if argv[i].startswith("-b"):
			print("         direkt Buecher Lesen ....")
			task="buecher"
			print (LINE)
		if argv[i].startswith("-p"):
			print("         Power Check nicht starten ....")
			power_check=False
			print (LINE)
		if argv[i].startswith("-t"):
			print("         Termin Check nicht starten ....")
			termin_check=False
			print (LINE)
	#
	dev=getDevice(debug)
	#
	# init pygame for sound
	#
	# good sound parameters for raspi
	# maybe get later from config file or database
	#
	frequency=48000
	size=-16
	channels=1
	buffer=1024
	speed=100
	voice='de'

	if pygame.mixer.get_init() is None:
		pygame.mixer.init(frequency, size, channels, buffer)

	Teddy(dev,task,debug)

if __name__ == "__main__":
    main()

