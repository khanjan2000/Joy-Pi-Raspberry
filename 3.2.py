import main
from main import field_6_c,field_7_1
import RPi.GPIO as RPi

import dht11
import queue
import time

RPi.setwarnings(False)
RPi.setmode(RPi.BCM)
RPi.cleanup()
#q_temp = queue.Queue(100)
#q_temp.put(field_6_1)
q_temp = field_6_c
q_humudity = field_7_1
num_elements_to_be_last_print = 3
while True:
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()
    print("temp: %-3.1f C" %result.temperature)
    print("humidity: %-3.1f %%" %result.humidity)
    temp = result.temperature
    humidity = result.humidity
    q_temp.append(temp)
    q_temp.pop(0)
    q_humudity.append(humidity)
    q_humudity.pop(0)
    #print(q_temp[-1])    #print last values for check of queue deque functionality
    #print(len(q_temp))   #printig length to get updated array len



    time.sleep(10)