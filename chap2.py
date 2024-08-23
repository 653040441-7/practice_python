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

# a,b,c = [float(e) for ]