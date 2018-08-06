#!/usr/bin/python2.7
# coding: utf8
# 
# Teddy - the interactive Hedgehog teddy bear client
# 
# (c) Michael Wntersperger 2018
#
teddy_version="0.12"
# 
from evdev import InputDevice, categorize, ecodes
from select import select
#
teddy_home="."
teddy_sounds="%s/sounds/" % teddy_home
teddy_books="%s/books/" % teddy_home
import os
if os.path.exists("/home/pi"):
	teddy_home="/home/pi/Teddy/Teddy"
	teddy_sounds="/home/pi/Teddy/Teddy/sounds/"
	teddy_books="/home/pi/Teddy/Teddy/books/"
import sys
import signal
import random
import pygame
import time
import threading
import psycopg2
#
from espeak import espeak, core
from datetime import datetime
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
# currently unused sound parameters
#
amplitude=100
word_gap=10
capitals=1
line_length=1
pitch=50
speed=175
spell_punctuation=[]

import threading

def do_every (interval, worker_func, debugging, iterations = 0):
	if debugging:
		print("### with debugging ...")
	if iterations != 1:
		threading.Timer (
			interval,
			do_every, [interval, worker_func, debugging, 0 if iterations == 0 else iterations-1]
		).start ()
	worker_func(debug=debugging)

class Power(object):
	def __init__(self, debug=False):
		self.sysfile="/sys/class/power_supply/BAT0/status"
		if not os.path.exists(self.sysfile):
			return
		self.debug=debug
		self.checkPower()

	def checkPower(self):
		f=open(self.sysfile,"r")
		status=f.readline()
		f.close()
		status=status.replace("\n","").replace("\l","")
		if status=="Full":
			if self.debug:
				print("### POWER STATUS OK: %s" % status)
			return True
		else:
			if self.debug:
				print("### POWER STATUS NOT OK: %s" % status)
			coutput("Batterie ist leer")
			return False

def wait4pygame():
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(10)

def wait4espeak(r):
	done_synth = [False]
	def cb(event, pos, length):
		if event == espeak.core.event_MSG_TERMINATED:
#			print("eSpeak DONE")
			done_synth[0] = True
	espeak.set_SynthCallback(cb)
	while r and not done_synth[0]:
		time.sleep(0.10)

def coutput(text, debug=True, voice="de"):
	print(">>>>>>>> %s" % text)
	mp3=teddy_sounds+text.replace(" ","_").replace("ü","ue").replace("ß","ss").replace("ö","oe").replace("ä","ae")+".mp3"
	if debug:
		print("### %s" % mp3)
	if os.path.exists(mp3):
		if debug:
			print(">>>>> found %s" % mp3)
		pygame.mixer.music.load(mp3)
		pygame.mixer.music.play()
		pygame.mixer.music.set_volume(1.0)
		wait4pygame()
	else:
#		pygame.mixer.music.pause()
		# Deutsche Sprache ... schwere Sprache ...
		espeak.core.set_voice(voice)
		r=espeak.synth("   %s" % text)
		wait4espeak(r)
#		pygame.mixer.music.unpause()

def getDevice(silent=False):
	# suche nach Joystick device ...
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
		line=inputs.readline()
	inputs.close()
	device="/dev/input/%s" % dv

	if os.path.exists(device):
		dev = InputDevice(device)
	else:
		if not silent:
			print("         Input Device not available")
			print (LINE)
		return None
	device=str(dev)
	sp=[]
	sp=device.split(",")
	if not silent:
		print("         Device:  %s" % sp[0].replace("device","").lstrip().rstrip())
		print("         Name:    %s" % sp[1].replace("name","").replace("\"","").lstrip().rstrip())
		print (LINE)
	return dev

def getButton(dev, timeout=5, debug=False):
	if dev is None:
		dev=getDevice(True)
	Running=True
	now = int(time.time())
	end=int(now+timeout)
	if debug:
		print("### now %d end %d" % (now,end))
	while now < end:
#		if debug:
#			print("### now %d" % now)
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
#					print(categorize(event))
#					print("### Type %s Code %s Value %s" % (event.type,event.code,event.value))
		now = int(time.time())
	#
	# while has ended due to timeout ...
	#
	if debug:
		print("### Timeout")
	return TIMEOUT

class Notfall(object):
	def __init__(self):
		#
		# im Moment machen wir noch nicht viel ....
		#
		coutput("Notfall Notfall Notfall")

class Termin(object):
	def __init__(self,dev=None,name=None,datum=None, zeit=None,beschreibung=None,ort=None,hinweis=None,debug=False):
		self.debug=debug
		if self.debug:
			print("### Termin mit debug output ....")
		if dev is None:
			self.dev=getDevice(True)
		else:
			self.dev=dev
		self.name=name
		self.datum=datum
		self.zeit=zeit
		self.beschreibung=beschreibung
		self.ort=ort
		self.hinweis=hinweis
		self.checkTermin()

	def checkTermin(self):
		conn = None
		epoch=0
		if self.name is None and self.zeit is None and self.datum is None:
			#
			# wir greifen zur Selbsthilfe / Datenbank
			# 
#			try:
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
						if self.debug:
							print("Pille am MONTAG")
						self.meldeTermin()
					if self.dienstag and weekday==1:
						if self.debug:
							print("Pille am DIENSTAG")
						self.meldeTermin()
					if self.mittwoch and weekday==2:
						if self.debug:
							print("Pille am MITTWOCH")
						self.meldeTermin()
					if self.donnerstag and weekday==3:
						if self.debug:
							print("Pille am DONNERSTAG")
						self.meldeTermin()
					if self.freitag and weekday==4:
						if self.debug:
							print("Pille am FREITAG")
						self.meldeTermin()
					if self.samstag and weekday==5:
						if self.debug:
							print("Pille am SAMSTAG")
						self.meldeTermin()
					if self.sonntag and weekday==6:
						if self.debug:
							print("Pille am SONNTAG")
						self.meldeTermin()
					self.beschreibung=""
					self.ort=""
					self.hinweis=""
					if self.debug:
						print("PILLE: ", self.name,self.montag,self.dienstag,self.mittwoch,self.donnerstag,self.freitag,self.samstag,self.sonntag,self.anzahl,self.zeit)
					row = cur.fetchone()
				cur.close()
#			except (Exception, psycopg2.DatabaseError) as error:
#				print(error)
			if conn is not None:
				conn.close()
		else:
			#
			# melde was uebergeben wurde ...
			# 
			self.meldeTermin()

	def meldeTermin(self):
		seconds = (self.zeit.hour * 60 + self.zeit.minute) * 60 + self.zeit.second
		epoch=time.mktime(self.datum.timetuple())+seconds
		te = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')
		now = int(time.time())
		tn = datetime.fromtimestamp(now).strftime('%Y-%m-%d %H:%M:%S')
		if self.debug:
			print("epoch %d (%s) now %d (%s)" % (epoch, te, now, tn))
		# schlimmstenfalls wird Termin 2x angesagt
		if epoch >= (now-30) and epoch < (now+30): 
			coutput("Termin")
			coutput(self.name)
			coutput("um")
			coutput(str(self.zeit.hour))
			coutput("Uhr")
			coutput(str(self.zeit.minute))
			coutput("Minuten")
			if len(self.beschreibung) > 0:
				coutput("Beschreibung")
				coutput(self.beschreibung)
			if len(self.ort) > 0:
				coutput("Ort")
				coutput(self.ort)
			if len(self.hinweis) > 0:
				coutput("Hinweis")
				coutput(self.hinweis)
		else:
			if self.debug:
				print("Termin: ", self.name, self.datum, self.zeit, self.beschreibung, self.ort, self.hinweis)
				print("Schade, Termin ist nicht jetzt")
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
		speed=175
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
			self.dev=getDevice(True)
		else:
			self.dev=device
		#
		# start task directly is defined for debugging ...
		# 
		if self.task=="simon":
			SimonSagt(self.dev,self.task,self.debug)
		elif self.task=="buecher":
			BuecherLesen(self.dev,self.task,self.debug)
		else:
			self.betterAsk()

	def betterAsk(self):
		Laufen=True
		while Laufen:
			if self.repeat < 5: # don't ask forever ...
				coutput("Wollen sie Simon Sagt spielen dann drücken sie den Rechten Arm")
				coutput("Wollen sie Hörbuecher hören dann drücken sie den linken Arm")
				self.repeat+=1
			pressed=getButton(self.dev, 10)
			if pressed==RECHTER_ARM:
				self.repeat=0
				if self.debug:
					print("### Starte Simon Sagt")
				SimonSagt(self.dev, self.task, self.debug)
				self.repeat=0
			elif pressed==LINKER_ARM:
				self.repeat=0
				if self.debug:
					print("### Starte Bücher Lesen")
				BuecherLesen(self.dev, self.task, self.debug)
				self.repeat=0
			elif pressed==NOTFALL:
				self.repeat=0
				if self.debug:
					print("### Notfall")
				Notfall()
				self.repeat=0
			elif pressed==BEENDEN:
				self.repeat=0
				if self.debug:
					print("### Beenden")
				Laufen=False
				self.repeat=0
			else:
				# TIMEOUT or not (yet) used button ...
				if self.debug:
					print("### noch nichts ...")
		if self.debug:
			print("### Teddy wurde beendet")
		coutput("Teddy wurde beendet")
		os._exit(0)

class LeseBuch(object):
	def __init__(self,dev=None,name=None,author=None,genre=None,path=None,ausgewaehlt=False,pausiert=False,vorgelesen=0, debug=False):
		self.debug=debug
		if self.debug:
			print("### Lese Buch mit debug output ....")
		if dev is None:
			self.dev=getDevice(True)
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
	
		self.runVorlesen()

	def runVorlesen(self):
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
				coutput("Rechter Arm beginne beim letzten Stop")
				coutput("Linker Arm beginne vom Anfang")
				Check=True
				while Check:
					pressed=getButton(self.dev, 10)
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
	
			coutput("Rechter Arm drücken Vorlesen pausieren")
			coutput("Beenden drücken Vorlesen beenden")

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
					pressed=getButton(self.dev, 1)
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
							coutput("Vorlesen pausiert")
							coutput("Rechter Arm weiter Vorlesen")
							now = int(time.time())
							lesezeit=now-start
							self.vorgelesen=self.vorgelesen+lesezeit
							vorgelesen=self.updateBuch(self.name, self.author, self.genre, mp3, self.ausgewaehlt, Paused, self.vorgelesen)
							if self.debug:
								print("### Paused %s after %d seconds" % (mp3,self.vorgelesen))
						
							pygame.mixer.stop()
							Paused=True
						else: # Paused
							coutput("Weiter vorlesen")
							coutput("Rechter Arm Pause beim Vorlesen")
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

	def updateBuch(self, name, author, genre, path, ausgewaehlt, pausiert, vorgelesen):
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
				if self.debug:
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

class BuecherLesen(object):
	def __init__(self,dev=None, task=None, debug=False):
		self.debug=debug
		if self.debug:
			print("### Buecher Lesen mit debug output ....")
		if dev is None:	
			self.dev=getDevice()
		else:
			self.dev=dev
		self.task=task
		
		self.runLesen()

	def runLesen(self):
		if self.debug:
			print("### Bucher Lesen wurde gestartet ....")
		Lesen=True
		coutput("Sie haben Bücher lesen ausgewählt")
		coutput("Linker Arm weiter")
		coutput("Rechter Arm auswählen")
		while Lesen:
			for author in os.listdir(teddy_books):
				while Lesen:
					if self.debug:
						print(">>>> %s" % author)
					coutput(author.replace("_"," "))
					pressed=getButton(self.dev, 5)
					if pressed==RECHTER_ARM:
						if self.debug:
							print("### Starte %s" % author)
						coutput(author.replace("_"," "))
						coutput("wurde ausgewählt")
						coutput("Linker Arm weiter")
						coutput("Rechter Arm auswählen")
						while Lesen:
							for buch in os.listdir("%s%s" % (teddy_books,author)):
								if buch.endswith(".mp3"):
									if self.debug:
										print(">>>> %s" % buch)
									coutput(buch.replace("_"," ").replace(".mp3",""))
									pressed=getButton(self.dev)
									if pressed==RECHTER_ARM:
										if self.debug:
											print("### Starte %s" % buch)
										coutput(buch.replace("_"," ").replace(".mp3",""))
										coutput("wurde ausgewählt")
										LeseBuch(self.dev,buch.replace(".mp3",""),author,debug=self.debug)
										Lesen=False
										break
	
									elif pressed==LINKER_ARM:
										if self.debug:
											print("### Weiter")
		#								break
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
		coutput("Hörbuecher hören wurde beendet")

class SimonSagt(object):
	def __init__(self,dev=None, task=None, debug=False):
		if dev is None:
			self.dev=getDevice(True)
		else:
			self.dev=dev
		self.task=task
		self.debug=debug
		if self.debug:
			print("### Simon Sagt mit debug output ....")
		coutput("Sie haben Simon Sagt ausgewaehlt")
		self.name="Simon Sagt"

		self.runSpiel()

	def runSpiel(self):
		if self.debug:
			print("### Simon sagt wurde gestartet ....")
		coutput("Simon Sagt Regeln")
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
				coutput("Simon sagt")
				if limb >= 1 and limb < 25:
					coutput("drücke meinen rechten Arm")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==RECHTER_ARM:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 25 and limb < 50:
					coutput("drücke meinen linken Arm")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==LINKER_ARM:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 50 and limb < 75:
					coutput("drücke meinen rechten Fuß")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==RECHTES_BEIN:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 75 and limb < 100:
					coutput("drücke meinen linken Fuß")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==LINKES_BEIN:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
			else:	# NO Simon says
				if limb >= 1 and limb < 25:
					coutput("drücke meinen rechten Arm")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 25 and limb < 50:
					coutput("drücke meinen linken Arm")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 50 and limb < 75:
					coutput("drücke meinen rechten Fuß")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
				elif limb >= 75 and limb < 100:
					coutput("drücke meinen linken Fuß")
					pressed=getButton(self.dev)
					if pressed==NOTFALL:
						Notfall()
						break
					elif pressed==BEENDEN:
						break
					elif pressed==TIMEOUT:
						coutput("Richtig")
						self.punkte+=1
					else:
						coutput("Falsch")
						self.punkte-=1
		if self.debug:
			print("Beende Simon Sagt")
		coutput("Simon Sagt wurde beendet")
		print(">>>> FINALE PUNKTE: %d" % self.punkte)
		self.updateSpiel()
		coutput("Sie haben")
		coutput(str(self.punkte))
		coutput("Punkte")
		if self.hoechststand < self.punkte:
			coutput("neuer Höchststand")
		else:
			coutput("Höchststand")
			coutput(str(self.hoechststand))
			coutput("Punkte")

	def updateSpiel(self):
#
#		insert a new gelesen value into the Spiele table
#
# 		Table Spiele(
#     		name varchar(255) PRIMARY KEY,
#        	punkte integer)
#
		name=self.name.replace("_"," ")
		points=str(self.punkte)
		self.hoechststand=0

		select= """SELECT * FROM Spiele WHERE name = %s;"""
		sql = """INSERT INTO Spiele(name,punkte)
             VALUES(%s,%s) RETURNING name;"""
		update = """UPDATE Spiele set punkte = %s WHERE name = %s;"""
		conn = None
		name_id = None
		try:
			conn = psycopg2.connect("dbname=teddy")
			# create a new cursor
			cur = conn.cursor()
			cur.execute(select, ((name,)))
			row = cur.fetchone()
			if row is not None:
				self.hoechststand=int(row[1])
				if self.debug:
					print("### hoechststand %d Punkte %d" % (self.hoechststand, self.punkte))
				if self.punkte > 0 and self.hoechststand < self.punkte:
					print(">>>>>>>> updating name %s hoechststand %d to %s" % (name,self.hoechststand, points))
					cur.execute(update, (points,name))
			else:
				# execute the INSERT statement
				cur.execute(sql, (name,points))
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

def signal_handler(signal, frame):
	print("\n")
	coutput("Teddy wurde beendet")
	os._exit(0)

def main():
	print (LINE)
	print ("                   >>>>>>>>>> Teddy V%s <<<<<<<<<<<" % teddy_version)
	print (LINE)
	debug=False
	task="none"

#	t = datetime.now().strftime("%k %M")
#	espeak.synth("Teddybär gestartet um %s" % t,"de")

	power_check=True
	termin_check=True
	argv=sys.argv
	argc=len(sys.argv)
#	print(argv[0])
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
	dev=getDevice()
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
	speed=175
	voice='de'
	#
	if pygame.mixer.get_init() is None:
		pygame.mixer.init(frequency, size, channels, buffer)
	#
	if power_check:
		# call checkPower every 10 second, forever
		do_every (10.0, Power, debug)

	if termin_check:
		# call checkTermin every 30 second, forever
		do_every (30.0, Termin, debug)

	Teddy(dev,task,debug)

if __name__ == "__main__":
    main()

