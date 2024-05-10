#fuck off data miner
import time
import random
import winsound
from pygame import mixer
money = 0
downloadspeed = 5
def sigdownload():
    print("Loading Signal.")
    time.sleep(1)
    print("Loading Signal..")
    time.sleep(1)
    print("Loading Signal...")
    time.sleep(downloadspeed)
    print("Signal downloaded! Use command siginf to know what you got!")
menu = input("Welcome to Signal Simulator! A text based VotV inspired game, type 1 for the tutorial, or type 2 for the main game. ")
if menu == "1":
    print("Welcome to the tutorial!")
    time.sleep(1)
    print("The commands are:")
    time.sleep(1)
    print("signals")
    print("get")
    print("play")
    print("save")
    print("siginf")
    print("quit")
    print("sell")
    print("balance")
    print("upgrade")
    print("Use get to get a signal, and while you have a signal, use sell to sell it, play to play it, or siginf to learn about the signal, and you can use upgrade to upgrade your stats!")
    print("Make a signal to finish the tutorial!")
    while True:
        tutorialcmd = input("Command: ")
        if tutorialcmd == "get":
            print("its buggy if i make a loading screen here fuck you")
            signalid = (random.randint(2, 2))
        if tutorialcmd == "siginf":
            if signalid == 2:
                print("Type: Planet")
                print("Value: 0")
        if tutorialcmd == "play":
            if signalid == 2:
                winsound.Beep(100, 100)
                print("T")
                winsound.Beep(200, 100)
                print("E")
                winsound.Beep(300, 100)
                print("X")
                winsound.Beep(400, 100)
                print("T")
                winsound.Beep(500, 100)
                print(" ")
                winsound.Beep(600, 100)
                print("H")
                winsound.Beep(700, 100)
                print("E")
                winsound.Beep(800, 100)
                print("R")
                winsound.Beep(900, 100)
                print("E")
                winsound.Beep(1000, 100)
        if tutorialcmd == "save":
            if signalid == 2:
                f = open("signals.txt", "a")
                f.write("tutorial\n")
                print("Signal saved!")
if menu == "2":
    while True:
        cmd = input("Command: ")
        if cmd == "get":
            sigdownload()
            signalid = (random.randint(0,2))
        if cmd == "siginf":
            if signalid == 0:
                print("Type: Unknown")
                print("Value: -1")
            if signalid == 1:
                print("Type: Planet")
                print("Value: 3")
            if signalid == 2:
                print("Type: Unknown")
                print("Value: 5")
        if cmd == "play":
            if signalid == 0:
                winsound.Beep(2000, 100)
                winsound.Beep(1000, 100)
                winsound.Beep(200, 100)
                print("g")
                winsound.Beep(200, 500)
                print("e")
                winsound.Beep(200, 500)
                print("t")
                winsound.Beep(200, 500)
                print("")
                winsound.Beep(200, 500)
                print("f")
                winsound.Beep(200, 500)
                print("u")
                winsound.Beep(200, 500)
                print("c")
                winsound.Beep(200, 500)
                print("k")
                winsound.Beep(200, 500)
                print("e")
                winsound.Beep(200, 500)
                print("d")
                winsound.Beep(200, 500)
                print(":trollface:")
            if signalid == 1:
                winsound.Beep(1000, 500)
                print("[")
                winsound.Beep(400, 200)
                print("N")
                winsound.Beep(2500, 400)
                print("O")
                winsound.Beep(100, 750)
                print(" ")
                winsound.Beep(700, 70)
                print("T")
                winsound.Beep(890, 350)
                print("E")
                winsound.Beep(1800, 500)
                print("X")
                winsound.Beep(670, 750)
                print("T")
            if signalid == 2:
                mixer.init()
                mixer.music.load('fart-with-reverb.mp3')
                mixer.music.play()
        if cmd == "save":
            if signalid == 0:
                f = open("signals.txt", "a")
                f.write("getFucked\n")
                f.close()
                print("Signal saved!")
            if signalid == 1:
                f = open("signals.txt", "a")
                f.write("planet01\n")
                f.close()
                print("Signal saved!")
            if signalid == 2:
                f = open("signals.txt", "a")
                f.write("fard\n")
                f.close()
                print("Signal saved!")
        if cmd == "signals":
            f = open("signals.txt", "r")
            print(f.read())
        if cmd == "quit":
            quit(0)
        if cmd == "sell":
            if signalid == 0:
                money = int(money) - 1
                signalid = 999999999
                print("You successfully got fucked! (-1 money)")
            if signalid == 1:
                money = int(money) + 3
                signalid = 999999999
                print("You successfully sold the signal! (+3 money)")
        if cmd == "balance":
            print(money)
        if cmd == "upgrade":
            print("Download Speed (Cost: 10 Money)")
            upgrade = input("Upgrade ")
            if upgrade == "Download Speed" or "download speed":
                if downloadspeed == 0:
                    print("That upgrade is at max level!")
                elif int(money) > 10:
                    downloadspeed = int(downloadspeed) - 1
                    money = int(money) -10
                else:
                    print("Sorry, you dont have enough money!")