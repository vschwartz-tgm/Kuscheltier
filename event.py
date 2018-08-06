#!/usr/bin/python3.6
from evdev import InputDevice, categorize, ecodes
from select import select
#
print("\n\nevent.py is just for testing joystick controller events and buttons ...\n\n")
#
# suche nach Joystick device ...
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
		line=inputs.readline()
	line=inputs.readline()

inputs.close()
device="/dev/input/%s" % dv
print("Joystick device: %s\n\n" % device)
print("now press buttons or move joystick ...\n\n")

dev = InputDevice(device)
while True:
	r,w,x = select([dev], [], [])
	for event in dev.read():
		if event.type == 3 and event.code == 1 and event.value == 255:
			print(">>> Rechter Arm")
		elif event.type == 3 and event.code == 1 and event.value == 0:
			print(">>> Linker Arm ")
		elif event.type == 3 and event.code == 0 and event.value == 255:
			print(">>> Rechtes Bein")
		elif event.type == 3 and event.code == 0 and event.value == 0:
			print(">>> Linkes Bein")
		elif event.type == 1 and event.code == 288 and event.value == 1:
			print(">>> Beenden")
		elif event.type == 1 and event.code == 305 and event.value == 1:
			print(">>> Beenden")
		elif event.type == 1 and event.code == 304 and event.value == 1:
			print(">>> Notfall")
		elif event.type == 1 and event.code == 289 and event.value == 1:
			print(">>> Notfall")
		else: #
			pass
#			print(categorize(event))
#			print("Type %s Code %s Value %s" % (event.type, event.code,event.value))
