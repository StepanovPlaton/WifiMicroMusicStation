class LogWriter:
    def __init__(self, PathToLog="/logs/log.txt"):
        self.PathToLog = PathToLog
        self.LogFile = open(self.PathToLog, "a")
        self.LogFile.write("\n ----- ----- ----- \n")
        self.LogFile.close()
    def Write(self, Message, Type, DateTime=None):
        self.LogFile = open(self.PathToLog, "a")
        self.LogFile.write(" (" + Type + ") ")
        if(DateTime is None): self.LogFile.write("UNKNOWN - ")
        else: 
            self.LogFile.write(str(DateTime[2]))
            self.LogFile.write("-")
            self.LogFile.write(str(DateTime[1]))
            self.LogFile.write("-")
            self.LogFile.write(str(DateTime[0]))
            self.LogFile.write(" ")
            self.LogFile.write(str(DateTime[3]))
            self.LogFile.write(":")
            self.LogFile.write(str(DateTime[4]))
            self.LogFile.write(" - ")
        self.LogFile.write(Message + "\n")
        self.LogFile.close()

    def ResetLog(self): open(self.PathToLog, 'w').close()