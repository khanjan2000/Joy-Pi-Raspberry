# We have digital scale=0 to 65535 and analog=-55 to 125 degree celcius.
# Find value of any digital no. in analog scale
digital=input("provide value")
c=float(digital)
cmin=0
cmax=65535
tempmin=-55
tempmax=125

#define scaling

temprange=tempmax-tempmin
temp=c*(temprange/cmax)+tempmin
print(temp)
