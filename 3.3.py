from main import field_3_1,field_2_1

def pm10_aqi(x):
    if 0 <= x <= 54.0:
        calc_aqi = (((50-0)*(x-0))/(54-0)) + 0
    elif 55 <= x <= 154:
        calc_aqi = (((100-51)*(x-55))/(154-55)) + 51
    elif 155 <= x <= 254:
        calc_aqi = (((150-101)*(x-155))/(254-155)) + 101
    elif 255 <= x <= 354:
        calc_aqi = (((200-151)*(x-255))/(354-255)) + 151
    elif 355 <= x <= 424:
        calc_aqi = (((300-201)*(x-355))/(424-355)) + 201
    elif 425 <= x <= 504:
        calc_aqi = (((400-301)*(x-425))/(504-425)) + 301
    elif 505 <= x <= 604:
        calc_aqi = (((500-401)*(x-505))/(604-505)) + 401
    calc_aqi = "{:.2f}".format(calc_aqi)
    return calc_aqi

def pm25_aqi(x):
    if 0 <= x <= 12.0:
        calc_aqi = (((50-0)*(x-0))/(12-0)) + 0
    elif 12.1 <= x <= 35.4:
        calc_aqi = (((100-51)*(x-12.1))/(35.4-12.1)) + 51
    elif 35.5 <= x <= 55.4:
        calc_aqi = (((150-101)*(x-35.5))/(55.5-35.5)) + 101
    elif 55.5 <= x <= 150.4:
        calc_aqi = (((200-151)*(x-55.5))/(150.4-55.5)) + 151
    elif 150.5 <= x <= 250.4:
        calc_aqi = (((300-201)*(x-150.5))/(250.4-150.5)) + 201
    elif 250.5 <= x <= 350.4:
        calc_aqi = (((400-301)*(x-250.5))/(350.4-250.5)) + 301
    elif 350.5 <= x <= 500.4:
        calc_aqi = (((500-401)*(x-350.5))/(500.4-350.5)) + 401
    calc_aqi = "{:.2f}".format(calc_aqi)
    return calc_aqi
aqi_pm25 = []
for i in field_2_1:
    v = pm25_aqi(i)
    aqi_pm25.append(v)
aqi_pm10 = []
for i in field_3_1:
    v = pm10_aqi(i)
    aqi_pm10.append(v)
print(aqi_pm10)
print(aqi_pm25)


