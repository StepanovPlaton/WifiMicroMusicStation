from time import sleep
import network

from MediaPlayer import MediaPlayerClass
from MicroDFPlayer import Player as MicroPlayer
from MicroServer import MicroPyServer

wlan_id = "home"
wlan_pass = "DWLSeaNet302WPA"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.ifconfig(('192.168.32.240','255.255.0.0','192.168.32.1','8.8.8.8'))
if not wifi.isconnected():
    wifi.connect(wlan_id, wlan_pass)

index_html_file = open("../web/index.html")
index_html = index_html_file.read()
index_html_file.close()

DFPlayerMiniCommander = MicroPlayer()
MediaPlayer = MediaPlayerClass(DFPlayerMiniCommander, 4, FileLimit=5)

def index(request): SendIndex()
def SendIndex(): server.send(index_html, content_type="Content-Type: text/html")

def back(request): 
    MediaPlayer.Back()
    SendIndex()
def stop_play(request): 
    if(MediaPlayer.Playing): MediaPlayer.Play()
    else: MediaPlayer.Stop()
    SendIndex()
def next(request): 
    MediaPlayer.Next()
    SendIndex()
def louder(request): 
    MediaPlayer.Louder()
    SendIndex()
def quieter(request): 
    MediaPlayer.Quieter()
    SendIndex()

server = MicroPyServer()

server.add_route("/", index)
server.add_route("/back", back)
server.add_route("/stop_play", stop_play)
server.add_route("/next", next)
server.add_route("/louder", louder)
server.add_route("/quieter", quieter)
server.start()
