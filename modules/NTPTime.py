import ntptime, time

class NTPTimeClass:
    def __init__(self): self.Sync()
    def Sync(self): ntptime.settime()
    def GetNTPTime(self):
        return list(time.localtime())