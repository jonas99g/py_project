import datetime
from time import sleep, strftime
import os
import requests

sensor_1 = "/sys/bus/w1/devices/28-0308979412dd/w1_slave"
sensor_2 = "/sys/bus/w1/devices/28-011623289bee/w1_slave"

end = datetime.datetime(2019, 7, 30, 18, 0, 0, 0)
channel_id = 828473
write_key = "VVIQII327TSA3FFA"


def measureTemp():
    field1 = "NAN"
    field2 = "NAN"
    field3 = "NAN"
    try:
        field1 = strftime("%Y-%m-%d %H:%M:%S")
        with os.popen(sensor_1) as d2:
            file2 = d2.read()
            value2 = file2.split("\n")[1].split(" ")[9]
            field2 = float(value2[2:]) / 1000
            d2.close()
        #with os.popen(sensor_2) as d2:
        #    for line in d1:
        #        field3 = str(line)
        requests.post('https://api.thingspeak.com/update.json?api_key=',write_key,"&field1=",field1,"&field2=",field2)
    except:
        print("Connection failed")

if __name__ == "__main__":
    while True:
        measureTemp()
        time.sleep(15)
        if end < datetime.datetime.now():
            break