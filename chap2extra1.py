p1,p2,p3,n1,n2 = [int(e) for e in input().split()]
a = 0
c = 0
if n1 <= p1 <= n2 :
    a += 10000
    
if n2//100 != n1//100:
   a += ((n2//100 - n1//100 ) - 1) * 25
   if n1%100 <= p2 :  
       a += 25
   if n2%100 >= p2:
       a += 25 
else : 
    if n1 % 100 <= p2 <= n2%100 :  
        a += 25
    else :
        print(n1 % 100, n2%100 )
    
if n2//1000 != n1//1000:
   a += ((n2//1000 - n1//1000 ) - 1) * 100
   if n1%1000 < p3: a += 100
   if n2%1000 > p3: a += 100
else : 
    if n1 % 1000 <= p3 <= n2%1000 :  
        a += 100
    else:
        print(n1 % 1000, n2%1000)
print(a)

            