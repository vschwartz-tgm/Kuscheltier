#!/usr/bin/python3.5

import random

class simonSagt(object):

    def __init__(self,highscore):
        self.highscore = highscore
        self.runSpiel()


    def runSpiel(self):
        print("Die Regeln sind einfach.")
        print("Wenn ich zum Beispiel sage 'Simon sagt das sie meine Linke Pfote drücken sollen', dann müssen sie dies machen.")
        print("Wenn ich das 'Simon sagt' weklasse sollen sie nichts machen")
        while True:
            zahl = random.randrange(1,100)
            limb = random.randrange(1,100)
            if zahl < 50:
                if limb >= 1 and limb < 25:
                    print("Simon sagt, drück meinen rechten Arm")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Rechter Arm":
                        print("Richtig");
                    else:
                        print("Falsch")
                elif limb >= 25 and limb < 50:
                    print("Simon sagt, drück meinen linken Arm")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Linker Arm":
                        print("Richtig");
                    else:
                        print("Falsch")
                elif limb >= 50 and limb < 75:
                    print("Simon sagt, drück meinen rechten Fuß")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Rechter Fuß":
                        print("Richtig");
                    else:
                        print("Falsch")
                elif limb >= 75 and limb < 100:
                    print("Simon sagt, drück meinen linken Fuß")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Linker Fuß":
                        print("Richtig");
                    else:
                        print("Falsch")
            elif zahl > 50:
                if limb >= 1 and limb < 25:
                    print("Drück meinen rechten Arm")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Nichts":
                        print("Richtig");
                    else:
                        print("Falsch")
                if limb >= 25 and limb < 50:
                    print("Drück meinen linken Arm")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Nichts":
                        print("Richtig");
                    else:
                        print("Falsch")
                if limb >= 50 and limb < 75:
                    print("Drück mein rechtes Beim")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Nichts":
                        print("Richtig");
                    else:
                        print("Falsch")
                if limb >= 75 and limb < 100:
                    print("Drück mein linkes Beim")
                    eingabe = input("Welchen Knopf wollen sie drücken?")
                    if eingabe == "Nichts":
                        print("Richtig");
                    else:
                        print("Falsch")
