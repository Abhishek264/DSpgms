def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b / gcd(a, b)
a=int(input('enter one number:'))
b=int(input('enter another number:'))
print(lcm(6,9))