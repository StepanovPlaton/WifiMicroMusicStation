import machine
from time import sleep


class MediaPlayerClass:
    def __init__(self, Player, BusyPin, FileLimit, FolderLimit=0, Play=False):
        self.Playing = False
        self.Volume = 10
        
        self.PlayingFile = 1
        self.PlayingFolder = 1

        self.Player = Player
        self.BusyPin = machine.Pin(BusyPin, machine.Pin.IN)
        self.Noise = machine.ADC(0)

        self.SetVolume(self.Volume)
    
        self.FileLimit = []
        self.FileLimit = FileLimit

        self.FolderLimit = FolderLimit

        if(Play): self.Play()

    def Play(self): 
        if(self.PlayingFile > self.FileLimit[self.PlayingFolder]): raise ValueError("Invalid file number!")
        if(not self.Playing):
            self.SetVolume(self.Volume)
            self.Player.play(self.PlayingFolder, self.PlayingFile)
            self.Playing = True
    def Stop(self): 
        if(self.Playing):
            self.SetVolume(0)
            self.Playing = False

    def PlayFile(self):
        if(self.PlayingFile > self.FileLimit[self.PlayingFolder]): raise ValueError("Invalid file number!")
        self.Playing = True
        self.Player.play(self.PlayingFolder, self.PlayingFile)

    def Next(self):
        self.PlayingFile += 1
        if(self.PlayingFile > self.FileLimit[self.PlayingFolder]): self.NextFolder()  
        if(self.PlayingFile <= self.FileLimit[self.PlayingFolder]): self.PlayFile()
    def Back(self):
        self.PlayingFile -= 1
        if(self.PlayingFile < 1): self.BackFolder(self.FileLimit[self.PlayingFolder])
        if(self.PlayingFile >= 1): self.PlayFile()

    def NextFolder(self, file=1):
        self.PlayingFolder += 1
        self.PlayingFile = file
        if(self.PlayingFolder > self.FolderLimit): self.PlayingFolder = 1
        self.PlayFile()
    def BackFolder(self, file=1):
        self.PlayingFolder -= 1
        self.PlayingFile = file
        if(self.PlayingFolder < 1): self.PlayingFolder = self.FolderLimit
        self.PlayFile()

    def Louder(self):
        self.Volume+=1
        self.SetVolume(self.Volume)
    def Quieter(self):
        self.Volume-=1
        self.SetVolume(self.Volume)
    def SetVolume(self, volume):
        self.Volume = volume
        self.Player.volume(self.Volume/30)
        sleep(0.5)

