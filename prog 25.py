
#printing feiajdoijadi numbers
a,b = 1,2
s = 0
print(a,end=',')
while b < 4000000:
    a,b = b,a+b
    print(a,end=',')
    if a%2 == 0:
            s += a
print()
print("Sum=",s)
