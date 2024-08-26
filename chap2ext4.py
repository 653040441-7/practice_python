h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
#  cal time parking
sumh = h2 - h1
summ = m2 - m1
sum = sumh*60 + summ
cost = 0
if sum <= 15 :
    cost = 0
elif 15 < sum <=180 :
    cost += 10*sumh
    if summ != 0 :
        cost +=10
elif  180<= sum <= 360 :
    cost += 20*(sumh - 3) + 10*3
    if summ != 0 :
        cost +=20
elif sum > 360 :
    cost = 200
print(cost)