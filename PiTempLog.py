import datetime
from time import sleep, strftime
import os
import requests

sensor_1 = "/sys/bus/w1/devices/28-011623289bee/w1_slave"
sensor_2 = "/sys/bus/w1/devices/28-011623289bee/w1_slave"

end = datetime.datetime(2019, 7, 30, 18, 0, 0, 0)
channel_id = 828473
write_key = "VVIQII327TSA3FFA"


def measureTemp()
    field1 = "NAN"
    field2 = "NAN"
    field3 = "NAN"
    try:
        field1 = strftime("%Y-%m-%d %H:%M:%S")
        with os.popen(sensor_2) as d1:
            for line in d1:
                field2 = str(line)
        with os.popen(sensor_2) as d2:
            for line in d1:
                field3 = str(line)
        requests.post('https://api.thingspeak.com/update.json?api_key=',write_key,"&field1=",field1,"&field2=",field2,"&field3=",field3)
    except:
        print("Connection failed")

if __name__ == "__main__":
    while True:
        measureTemp()
        time.sleep(15) # free account has an api limit of 15sec
        if end < datetime.datetime.now():
            break