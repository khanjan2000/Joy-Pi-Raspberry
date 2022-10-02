import requests
#import pandas as pd
from time import sleep
from matplotlib import pyplot as plt
from statistics import mean
import json
import numpy as np
r = requests.get('https://api.thingspeak.com/channels/628559/feeds.json?result=100')

#print(r.text)
test = json.loads(r.text)
feeds = test['feeds']
field_1 = []
field_2 = []
field_3 = []
field_4 = []
field_5 = []
field_6 = []
field_7 = []
field_8 = []
for x in range(99):
    x = x + 1
    data = feeds[x]['field1']
    field_1.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field2']
    field_2.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field3']
    field_3.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field4']
    field_4.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field5']
    field_5.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field6']
    field_6.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field7']
    field_7.append(data)
for x in range(99):
    x = x + 1
    data = feeds[x]['field8']
    field_8.append(data)
print(field_1)
field_1_1 = list(map(float,field_1))
mean_field_1 = mean(field_1_1)
print(mean_field_1)
field_2_1 = list(map(float,field_2))
mean_field_2 = mean(field_2_1)
print(mean_field_2)
field_3_1 = list(map(float,field_3))
mean_field_3 = mean(field_3_1)
print(mean_field_3)
field_6_1 = list(map(float,field_6))
#convert temperature in degree celsius
field_6_c = []
for x in field_6_1:
    t = (x-32)*(5/9)
    field_6_c.append(t)
    x = x +1
field_6_c = list(map(float,field_6_c))

field_7_1 = list(map(float,field_7))


print("here starts field 2")
print(field_2)
print("field 3 starts here")
print(field_3)
x_data = range(0,10)
y_data = x_data
y_data2  = range(10,20)
plt.subplot(3,1,1)
plt.plot(range(99),field_1_1,'rd-')
plt.axhline(y=mean_field_1,color = 'r',linestyle = '--')
plt.xlabel('sample')
plt.ylabel('ATM')
plt.title('PM 1.0')

plt.subplot(3,1,2)
plt.plot(range(99),field_2_1,'ko-')
plt.axhline(y=mean_field_2,color = 'black',linestyle = '--')
plt.xlabel('sample')
plt.ylabel('ATM')
plt.title('PM 2.5')

plt.subplot(3,1,3)
plt.plot(range(99),field_3_1,'bo-')
plt.axhline(y=mean_field_3,color = 'b',linestyle = '--')
plt.xlabel('sample')
plt.ylabel('ATM')
plt.title('PM 10')

plt.show()
