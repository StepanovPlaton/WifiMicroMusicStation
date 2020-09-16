from time import sleep
import network
import urandom

from MediaPlayer import MediaPlayerClass
from MicroDFPlayer import Player as MicroPlayer
from NTPTime import NTPTimeClass
from ConfigReader import ConfigReader
from LogWriter import LogWriter

def random():
    if(TimeWithMyTimeZone(NTPTime.GetNTPTime(), Config.TimeZone) is None):
        return urandom.getrandbits(5)**MediaPlayer.Noise.read()
    else:
        time = TimeWithMyTimeZone(NTPTime.GetNTPTime(), Config.TimeZone)
        return urandom.getrandbits(5)**MediaPlayer.Noise.read()*time[2]+time[5]**time[6]
def GenerateFolderNum(Config, FoldersAmount, Time):
    while True:
        FolderNum = (random() % FoldersAmount)+1
        try:
            if(Config[FolderNum-1][Time] == 1): return FolderNum
        except Exception: pass

def TimeWithMyTimeZone(Time, TimeZone):
    if(Time is None or TimeZone is None): return None
    Time[3] = (Time[3]+TimeZone) % 24
    return Time

NTPTime = NTPTimeClass()      
Log = LogWriter("/logs/log.txt")
Config = ConfigReader("/configs/config.txt")
if(len(Config.Errors) != 0):
    Log.Write("Ошибка(-и) загрузки конфига! :-(\n - ", "!!!ERROR!!!")
    for i in Config.Errors: Log.Write(i, "!!!ERROR!!!")
    raise ValueError("Ошибка загрузки конфига! :-(")
else: Log.Write("Конфиг загружен! =-)", "CONFIG", TimeWithMyTimeZone(NTPTime.GetNTPTime(), Config.TimeZone))

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.ifconfig((Config.WLAN_static_ip, Config.WLAN_netmask, Config.WLAN_gateway, Config.WLAN_DNS_server))
if not wifi.isconnected():
    wifi.connect(Config.WLAN_id, Config.WLAN_password)

print(wifi.isconnected())
print(wifi.ifconfig())
sleep(2)
if(wifi.isconnected()): 
    NTPTime.Sync()
    if(NTPTime.GetNTPTime()[6] == 0): Log.ResetLog()
    Log.Write("Подключился к Wifi {0} с IP - {1}".format(Config.WLAN_id, Config.WLAN_static_ip), "Wifi", TimeWithMyTimeZone(NTPTime.GetNTPTime(), Config.TimeZone))
else:
    Log.Write("Не удалось подключится к Wifi!", "ERROR")
    raise ValueError("Не удалось подключится к Wifi!")

DFPlayerMiniCommander = MicroPlayer()
MediaPlayer = MediaPlayerClass(DFPlayerMiniCommander, 4, Config.FilesAmount, Config.FoldersAmount)

Log.Write("Соединение с плеером...", "PLAYER", TimeWithMyTimeZone(NTPTime.GetNTPTime(), Config.TimeZone))

while True:
    if(MediaPlayer.BusyPin.value() != 0):
        NTP = NTPTime.GetNTPTime()
        if(NTP is None):
            Time = None
        else:
            Time_ = NTP
            Time_ = TimeWithMyTimeZone(Time_, Config.TimeZone)
            Time = NTP[3]

        if(Time is None):
            MediaPlayer.SetVolume(Config.Volume[7 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 7 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time < 9):
            MediaPlayer.SetVolume(Config.Volume[1 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 1 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time < 12):
            MediaPlayer.SetVolume(Config.Volume[2 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 2 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time < 15):
            MediaPlayer.SetVolume(Config.Volume[3 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 3 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time < 18):
            MediaPlayer.SetVolume(Config.Volume[4 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 4 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time < 21):
            MediaPlayer.SetVolume(Config.Volume[5 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 5 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1
        elif(Time <= 23):
            MediaPlayer.SetVolume(Config.Volume[6 -1])
            MediaPlayer.PlayingFolder = GenerateFolderNum(Config.PlayingRules, Config.FoldersAmount, 6 -1)
            MediaPlayer.PlayingFile = (random() % MediaPlayer.FileLimit[MediaPlayer.PlayingFolder])+1

        mess = "Играем трек {0} из папки {1} с громкостью {2}".format(MediaPlayer.PlayingFile, MediaPlayer.PlayingFolder, Config.Volume[6 -1])
        Log.Write(mess, "NextTrack", Time_)
    
        MediaPlayer.PlayFile()

        sleep(1)
    else: sleep(1)