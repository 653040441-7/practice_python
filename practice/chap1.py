import math 

h,m,s = [int(e) for e in input().split()]
print(h*60**2 + m*60 + s)

x = float(input())
print(2 - x + 3* x**2 / 7 - 5 *x**3 / 11 + math.log(x,10))

a = float(input())
x = 1
x = (x + a/x) / 2
print(4*x)

v1,v2,v3 = [float(v) for v in input()]
u1,u2,u3 = [float(u) for u in input()]
print(v1*u1 + v2*u2 + v3*u3)

x1,y1,x2,y2 = [float(e) for e in input().split()]
print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

r,theta = [float(e) for e in input().split()]
print(r*math.cos(theta),r*math.sin(theta))

x , y = [float(e) for e in input().split()]
r = math.sqrt(x**2 + y**2)
theta = math.acos(x / r)
print(r,theta)

a,b,c,d,e = [float(e) for e in input().split()]
print((a+b+c+d+e)/5)

a,b,c = [str(e) for e in input().split()]
print(a+b+c+(a+b)*int(c))