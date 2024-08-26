
p = 0
for k in range(1,8,4):
    p += 1/k
    p -= 1/(k+2)
print(4*p)
    