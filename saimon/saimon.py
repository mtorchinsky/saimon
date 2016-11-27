from playsound import playsound
import time
import random 
import sys,tty,termios


class Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def getMove():
        inkey = Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                #print "up"
                return 2
        elif k=='\x1b[B':
                #print "down"
                return 4
        elif k=='\x1b[C':
                #print "right"
                return 3
        elif k=='\x1b[D':
                #print "left"
                return 1
        else:
                print "not an arrow key!"

class Saimon():
    def __init__(self, soundPath='.'):
        self.spanish = 1
        self.sequence = []
        self.soundPath = soundPath

        return
    
    def addItem(self):
        number = random.randint(1,3)
        if number == 1: 
            if self.spanish: wavname = 'cuchara.wav'
            else: wavname = 'spoon.wav'
        elif number == 2: 
            if self.spanish: wavname='tenedor.wav'
            else: wavname = 'fork.wav'
        elif number == 3: 
            if self.spanish: wavname='cuchillo.wav'
            else: wavname = 'knife.wav'
        else: 
            if self.spanish: wavname='todos.wav'
            else: wavname = 'alltogheter.wav'

        wavname = self.soundPath+wavname
        self.sequence.append((number,wavname))

        print number,wavname

        return
      

    def playOk(self):
        playsound(self.soundPath+'ok.wav')
        return

    def playGotIt(self):
        playsound(self.soundPath+'gotit.wav')
        return

    def playYouLoose(self):
        playsound(self.soundPath+'youloose.wav')
 
    def getSequence(self):
        return self.sequence

    def saySequence(self):
        for item in self.sequence:
            playsound(item[1])

        return

if __name__ == '__main__':
    looping = 1
    saimon = Saimon(soundPath='/Users/matt/Develop/saimon/sounds/')

    while (looping):
        saimon.addItem()
        saimon.saySequence()

        for index in saimon.getSequence():
            """ print "Move?:", """
            Input = getMove()
            if (index[0] != Input): 
                """
                print "Input:",Input,"Expected:",index
                """
                looping = 0
                saimon.playYouLoose()
                break
            else:
                saimon.playGotIt()

        if looping==1: 
            saimon.playOk()
            time.sleep(0.5)

