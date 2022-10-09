n = int(input('Enter n:'))

for i in range(1, n+2):
    for j in range(1, n+2-i):
        print("*", end='')
        j += 1
    print('\r')
    i += 1
