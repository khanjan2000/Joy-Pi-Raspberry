
import RPi.GPIO as RPi
import matplotlib.pyplot as plt
import dht11
from main import Temperature_c, Humidity
import queue
import time
Temperature_c = list(map(float,Temperature_c))

Humidity_1 = list(map(float,Humidity))
# from collections import deque

RPi.setwarnings(False)
RPi.setmode(RPi.BCM)
RPi.cleanup()
# q_temp = queue.Queue(100)
# q_temp.put(Temperature_c)
# q_humudity = Humidity_1
# num_elements_to_be_last_print = 3
while True:
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():
        result = instance.read()
    # print("temp: %-3.1f C" %result.temperature)
    # print("humidity: %-3.1f %%" %result.humidity)
    # temp = result.temperature
    r_temp = []
    r_humid = []
    for r in range(99):
        r += 1
        r_temp.append(result.temperature)
        r_humid.append(result.humidity)
    # humidity = result.humidity
    # q_temp.append(temp)
    r_temp.pop(0)
    r_humid.pop(0)
    print("temp is:", r_temp)
    print("humidity is:", r_humid)
    # q_humudity.append(humidity)

    # q_humudity.pop(0)
    # print(q_temp[-1])    #print last values for check of queue deque functionality
    # print(len(q_temp))   #printig length to get updated array len

   
#plotting
r_temp = list(map(float, r_temp))
r_humid = list(map(float, r_humid))

x_data = range(0, 10)
y_data = x_data
y_data2 = range(10, 20)
plt.subplot(5, 1, 4)
plt.plot(range(99), q_temp, 'bo-')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temp')

plt.subplot(5, 1, 5)
plt.plot(range(99), r_humid, 'bo-')
plt.xlabel('Date')
plt.ylabel('Humidity')
plt.title('Hum')

plt.show()

