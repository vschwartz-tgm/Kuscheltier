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

class Power(object):
	def __init__(self, debug=False):
		#
		from teddy import coutput
		#
		self.sysfile="/sys/class/power_supply/BAT0/status"
		if not os.path.exists(self.sysfile):
			return
		self.debug=debug
		self.checkPower(self.debug)

	def checkPower(self, debug=False):
		#
		# A Function that reads the file "/sys/class/power_supply/BAT0/status" and reads the status of the power supply.
		#
		# :return:
		#
		f=open(self.sysfile,"r")
		status=f.readline()
		f.close()
		status=status.replace("\n","").replace("\l","")
		if status=="Full":
			if debug:
				print("### POWER STATUS OK: %s" % status)
			return True
		else:
			if debug:
				print("### POWER STATUS NOT OK: %s" % status)
			coutput("Battery is empty")
			return False
