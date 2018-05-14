#!/usr/bin/python3.5
from evdev import InputDevice, categorize, ecodes
from select import select
dev = InputDevice('/dev/input/event0')
print(dev)
while True:
	r,w,x = select([dev], [], [])
	for event in dev.read():
		if event.type == 3 and event.code == 1 and event.value == 255:
			print(">>> Rechts Oben")
		elif event.type == 3 and event.code == 1 and event.value == 0:
			print(">>> Links Oben")
		elif event.type == 3 and event.code == 0 and event.value == 255:
			print(">>> Rechts Unten")
		elif event.type == 3 and event.code == 0 and event.value == 0:
			print(">>> Links Unten")
		else: #
			pass
#                       print(categorize(event))
#                       print "Type ", event.type, " Code ", event.code, " Value                                                                                                              ", event.value
