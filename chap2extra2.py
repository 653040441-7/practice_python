m, y = [int(e) for e in input().split()]
if m == 1 or m ==3 or m ==5 or m ==7 or m ==8 or m ==10 or m ==11 or m ==12:
    print(31)
elif m == 4 or m ==6 or m ==9 :
    print(30)
elif m == 2 :
    if ((y - 543)%4 == 0) and ((y - 543)%100 != 0) :
        print(29)
    else:
        print(28)
else:
    print('error')

