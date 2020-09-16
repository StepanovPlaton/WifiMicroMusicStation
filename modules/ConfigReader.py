class ConfigReader:
    def __init__(self, PathToConfig="/configs/config.txt"):
        self.PlayingRules = None

        self.FoldersAmount = None
        self.FilesAmount = None

        self.WLAN_id = None
        self.WLAN_password = None
        self.WLAN_static_ip = None
        self.WLAN_netmask = None
        self.WLAN_gateway = None
        self.WLAN_DNS_server = None

        self.TimeZone = None

        self.Volume = None

        RulesRead = False

        self.Errors = []

        ConfigFile = open(PathToConfig, "r")
        for i in ConfigFile:
            if(i[0] == "#"): continue
            if(i.split("=")[0].find("Folders") != -1): 
                self.FoldersAmount = int(i.split("=")[1])
                self.PlayingRules = []
                for j in range(self.FoldersAmount): self.PlayingRules.append([-1, -1, -1, -1, -1, -1, -1])
            if(i.split("=")[0].find("Files") != -1):
                self.FilesAmount = []
                if(i.split("=")[1].find("unknown") != -1):
                    if(self.FoldersAmount is None): self.Errors.append("Config read error - FoldersAmount is None")
                    for j in range(self.FoldersAmount): self.FilesAmount.append(200)
                else:
                    for j in i.split("=")[1].split(","): self.FilesAmount.append(int(j))
                if(self.FoldersAmount is not None):
                    if(len(self.FilesAmount) != self.FoldersAmount): 
                        self.Errors.append("Config read error - length FilesAmount does not match FoldersAmount")
                else: self.Errors.append("Config read error - FoldersAmount is None")

            if(i.split("=")[0].find("Volume") != -1):
                self.Volume = []
                for j in i.split("=")[1].split(","): self.Volume.append(int(j))
                if(len(self.Volume) != 7): self.Errors.append("Config read error - the number of timestamps must be 7")

            if(i.split("=")[0].find("TimeZone") != -1):
                self.TimeZone = int(i.split("=")[1].split(" ")[2].replace(" ", "").rstrip())
                if(i.split("=")[1].split(" ")[1].find("-") != -1): self.TimeZone *= -1

            if(i.split("=")[0].find("WLAN_id") != -1): self.WLAN_id = i.split("=")[1][1:].rstrip()
            if(i.split("=")[0].find("WLAN_password") != -1): self.WLAN_password = i.split("=")[1].replace(" ", "").rstrip()
            if(i.split("=")[0].find("WLAN_static_ip") != -1): self.WLAN_static_ip = i.split("=")[1].replace(" ", "").rstrip()
            if(i.split("=")[0].find("WLAN_netmask") != -1): self.WLAN_netmask = i.split("=")[1].replace(" ", "").rstrip()
            if(i.split("=")[0].find("WLAN_gateway") != -1): self.WLAN_gateway = i.split("=")[1].replace(" ", "").rstrip()
            if(i.split("=")[0].find("WLAN_DNS_server") != -1): self.WLAN_DNS_server = i.split("=")[1].replace(" ", "").rstrip()

            if(i.find("--- PLAY RULES ---") != -1): RulesRead = not RulesRead
            
            if(i[0] == "!" and RulesRead):
                folder = int(i[1:3])
                if(self.PlayingRules is None): 
                    self.Errors.append("Config read error - FoldersAmount must go before the rules playing")
                elif(folder > len(self.PlayingRules)): 
                    self.Errors.append("Config read error - The folder number in the right exceeds the number of folders")
                else:
                    data = i.split("=")[1].split("|")
                    if(len(data) != 7): self.Errors.append("Config read error - the number of gaps must be 7")
                    for j in range(len(data)): self.PlayingRules[folder-1][j] = int(data[j].replace(" ", "").rstrip())

        if(self.FoldersAmount is None or self.FilesAmount is None or
            self.WLAN_id is None or self.WLAN_password is None or
             self.WLAN_static_ip is None or self.WLAN_netmask is None or
              self.WLAN_gateway is None or  self.WLAN_DNS_server is None or 
               self.Volume is None or self.TimeZone is None): 
            self.Errors.append("Config read error - some values ​​are missing")
        
        ConfigFile.close()
