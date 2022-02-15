def connect():
    import network
    
    ssid = "HUAWEI Mate 20 Pro"
    password = "0432349128"
    
    station = network.WLAN(network.STA_IF)
    
    if station.isconnected() == True:
        print("Already Connected")
        return
    
    station.active(True)
    station.connect(ssid, password)
    
    while station.isconnected == False:
        pass
    
    print("Connection Sucessful")
    print(station.ifconfig())