def calgrade(s):
    if 0 <= s < 50:
        print('F')
    elif 50 <= s < 55:
        print('D')
    elif 55 <= s < 60:
        print('D+')
    elif 60 <= s < 65:
        print('C')
    elif 65 <= s < 70:
        print('C+')
    elif 70 <= s < 75:
        print('B')
    elif 75 <= s < 80:
        print('B+')
    elif 80 <= s <= 100:
        print('A')
    else:
        print('error')

    
a = calgrade(87.25)
a = calgrade(69.95)
a = calgrade(120)