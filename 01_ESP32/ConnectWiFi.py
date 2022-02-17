def connect():
    import network
    
    ssid = "your_wifi_id"
    password = "your_password"
    
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
