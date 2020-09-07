def prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def twins(start, end):
   for i in range(start, end):
      j = i + 2
      if(prime(i) and prime(j)):
         print(i,j)

twins(2,50)