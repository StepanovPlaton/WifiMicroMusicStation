# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

from time import sleep
import network
from ConfigReader import ConfigReader
from LogWriter import LogWriter

Log = LogWriter("/logs/log.txt")
Config = ConfigReader("/configs/config.txt")

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.ifconfig((Config.WLAN_static_ip, Config.WLAN_netmask, Config.WLAN_gateway, Config.WLAN_DNS_server))
if not wifi.isconnected():
    wifi.connect(Config.WLAN_id, Config.WLAN_password)

print(wifi.isconnected())
print(wifi.ifconfig(), Config.WLAN_id, Config.WLAN_password)