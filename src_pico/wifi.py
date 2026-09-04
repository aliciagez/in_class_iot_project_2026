import json
import network
import rp2
import time

rp2.country("SE")

with open("wifi_cred.json") as file:
    cre = json.load(file)



def connect_wifi(waiting_time = 10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(cre.get("SSID"), cre.get("PASSWORD"))

    while waiting_time > 0:
        if wlan.isconnected():
            print("connect")
            break

        waiting_time -= 1
        print("try to connect to wifu")
        time.sleep(2)

    return wlan.isconnected()

print(cre)