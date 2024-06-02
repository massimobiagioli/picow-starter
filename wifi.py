import config
import network


def connect(): 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(config.wifi["ssid"], config.wifi["password"])
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())