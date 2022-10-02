import RPi.GPIO as RPi
import requests
import dht11
import time
import json
from statistics import mean
from matplotlib import pyplot as plt

fields = requests.get("https://thingspeak.com/channels/628559/feed.json")
field_data = json.loads(fields.text)
feeds = field_data['feeds']
field_6 = []
field_7 = []
for a in range(99):
    a = a + 1
    data = feeds[a]['field6']
    field_6.append(data)
for b in range(99):
    b = b + 1
    data = feeds[b]['field7']
    field_7.append(data)

field_6a = list(map(float, field_6))
#convert temperature in degree celsius
field_6_c = []

for a in field_6a:
    t = (a-32)*(5/9)
    field_6_c.append(t)
    a = a + 1
field_6_indeg_c = list(map(float, field_6_c))
field_7a = list(map(float, field_7))
print(field_6_indeg_c)
print(field_7)

RPi.setwarnings(False)
RPi.setmode(RPi.BCM)
RPi.cleanup()
while True:
    # read data using pin 4
    instance = dht11.DHT11(pin=4)
    result = instance.read()
    while not result.is_valid():  # read until valid values
        result = instance.read()
    for y in range(99):
        y = y+1
        print(y)
        print("Temperature: %-3.1f C" % result.temperature)
        print("Humidity: %-3.1f %%" % result.humidity)
        temperature = result.temperature
        humidity = result.humidity
        field_6_indeg_c.append(temperature)
        field_6_indeg_c.pop(0)
        field_7.append(humidity)
        field_7.pop(0)
        time.sleep(0.25)
    break
mean_field_6_indeg_c = mean(field_6_indeg_c)
print(mean_field_6_indeg_c)
mean_field_7 = mean(field_7a)
print(mean_field_7)
plt.subplot(2,1,1)
plt.plot(range(99), field_6_indeg_c, 'rd-')
plt.axhline(y=mean_field_6_indeg_c, color='r', linestyle='--')
plt.xlabel('date')
plt.ylabel('Temperature')
plt.title('Temperature in Celsius')
plt.subplot(2,1, 2)
plt.plot(range(99), field_7a, 'bo-')
plt.axhline(y=mean_field_7, color='b', linestyle='--')
plt.xlabel('date')
plt.ylabel('Humidity')
plt.title('Humidity')
