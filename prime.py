low=int(input('Enter lower limit:'))
high=int(input('enter upper limit:'))
for num in range(low,high+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)

