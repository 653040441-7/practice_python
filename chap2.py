# point 1
a,b,c = [float(e) for e in input().split()]
if a > b : 
    if b > c :  
        med = b
    elif c > a :   
        med = a
    else: med = c
else:
    if b < c :  # b < c
        med = b
    elif c < a :   
        med = a
    else: med = c
print(med)

# point 2
import math
x1,y1,r1 = [float(e) for e  in input().split()]
x2,y2,r2 = [float(e) for e  in input().split()]
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if d > math.abs(r1+r2) :
    print('free')
elif d == r1+r2 :
    print('collision')
else:
    print('overlap')

# point 3
x,y = [float(e) for e in input().split()]
if x > 0 and y > 0 :
    print('1')
elif x > 0 and y < 0 :
    print('2')
elif x < 0 and y > 0:
    print('3')
elif x < 0 and y < 0:
    print('4')
elif x == 0 and y != 0:
    print('y-exis')
elif x != 0 and y == 0:
    print('x-exis')
else:
    print('origin')

# point 4
v,w,x,y,z = [float(e) for e in input().split()]
if x > w and x < y :
    if w > v and y < z:
        print('True')
    else: print('False')
else: print('False')

# point 5
import math
a = int(input())
x = int(round(a**(1/3),0))
if(x**3 == a):
    print(x)
else:
    print(x)

# point 6
a = int(input())
if a < 37 :
    s = 'XS' 
elif 36 < a < 41 :
    s = 'S'
elif 40 < a < 43 :
    s = 'M'
elif 42 < a < 46 :
    s = 'L'
elif 46 < a :
    s = 'XL'
print(s)

# point 7
p1,p2,p3,n1,n2 = [int(e) for e in input().split()]
if n1 <= p1 <= n2 :
    a += 10000  
print(n1//100)
print(n2//100)