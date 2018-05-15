#!/usr/bin/python3.5

from SimonSays import simonSagt

def main():
    while True:
        print("Drücken sie einen Knopf.")
        print("Wollen sie Simon Sagt spielen, dann drücken sie den Rechter Arm.")
        eingabe = input("Welchen Knopf wollen sie drücken?")
        if eingabe == "Rechter Arm":
            print("Sie haben, Simon Sagt ausgewählt.");
            spiel = simonSagt(highscore=0)
        elif eingabe == "Linker Arm":
            print(">>> Linker Arm")
        elif eingabe == "Rechter Fuß":
            print(">>> Rechter Fuß")
        elif eingabe == "Linker Fuß":
            print(">>> Linker Fuß")
        else: #
            pass
    #                       print(categorize(event))
    #                       print "Type ", event.type, " Code ", event.code, " Value                                                                                                              ", event.value



if __name__ == "__main__":
    main()
