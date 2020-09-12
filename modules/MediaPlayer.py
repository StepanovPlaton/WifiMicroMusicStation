import machine
from time import sleep

class MediaPlayerClass:
    def __init__(self, Player, BusyPin, PlayedLedPin=16, FileLimit=200, FloderLimit=3, Play=True):
        self.Playing = False
        self.Volume = 15
        self.PlayingFile = 1
        self.PlayingFloder = 1

        self.LoopFile = False
        self.LoopDirectory = False
        self.RandomFiles = False
        self.RandomFloders = False

        self.Player = Player
        self.Play_led = machine.Pin(PlayedLedPin, machine.Pin.OUT)
        self.BusyPin = machine.Pin(BusyPin, machine.Pin.IN)

        self.FileLimit = FileLimit
        self.FloderLimit = FloderLimit

        if(Play): self.Play()
    def Play(self): 
        if(not self.Playing):
            self.SetVolume(self.Volume)
            self.Player.play(self.PlayingFloder, self.PlayingFile)
            self.Playing = True
            self.Play_led.on()
    def Stop(self): 
        if(self.Playing):
            self.SetVolume(0)
            self.Playing = False
            self.Play_led.off()

    def PlayFile(self, Floder=None, File=None):
        self.SetVolume(self.Volume)
        self.Playing = True
        self.Play_led.on()
        self.Player.play(Floder if Floder else self.PlayingFloder, File if File else self.PlayingFile)

    def Next(self):
        self.PlayingFile += 1
        if(self.PlayingFile > self.FileLimit):
            if(self.LoopDirectory): 
                self.PlayingFile = 1
            else: self.NextFloder()  
        if(self.PlayingFile <= self.FileLimit or 
           self.PlayingFile > self.FileLimit and self.LoopDirectory):
            self.PlayFile()
    def Back(self):
        self.PlayingFile -= 1
        if(self.PlayingFile < 1): 
            if(self.LoopDirectory): self.PlayingFile = self.FileLimit
            else: self.BackFloder(self.FileLimit)
        if(self.PlayingFile >= 1 or self.PlayingFile < 1 and self.LoopDirectory):    
            self.PlayFile()

    def NextFloder(self, file=1):
        self.PlayingFloder += 1
        self.PlayingFile = file
        if(self.PlayingFloder > self.FloderLimit):
            self.PlayingFloder = 1
        self.PlayFile()
    def BackFloder(self, file=1):
        self.PlayingFloder -= 1
        self.PlayingFile = file
        if(self.PlayingFloder < 1):
            self.PlayingFloder = self.FloderLimit
        self.PlayFile()

    def Louder(self):
        self.Volume+=1
        self.SetVolume(self.Volume)
    def Quieter(self):
        self.Volume-=1
        self.SetVolume(self.Volume)
    def SetVolume(self, volume):
        self.Player.volume(self.Volume/30)
        sleep(0.1)
