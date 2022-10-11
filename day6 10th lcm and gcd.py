import math
n=int(input("enter the number of elements:"))
a = int(input('First Number :'))
b = int(input('Second Number :'))
c = int(input('Third Number :'))
gcd = math.gcd(a,b)
lcm = (a*b)/gcd
gcd = math.gcd(gcd,c)
lcm = (c*lcm)/gcd
print('gcd :',gcd) 
print('lcm :',lcm) 
