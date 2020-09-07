# program to accept a number and verify whether it is a number or not
x=input('Enter a number')
try:
    x=int(x)
    print('the given number is',x)
except:
    print('The given input',x, 'is not a number')

