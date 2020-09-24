import ntptime, time

class NTPTimeClass:
    def __init__(self): 
        self.TimeOk = False
        self.Sync()
    def Sync(self): 
        try: 
            ntptime.settime()
            self.TimeOk = True
        except Exception: self.TimeOk = False
    def GetNTPTime(self):
        if(self.TimeOk): return list(time.localtime())
        else: return None