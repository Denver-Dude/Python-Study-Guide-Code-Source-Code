
def fib(upperlimit):
    global flist
    flist = list()
    a,b = 1,2
    while a< upperlimit:
        flist.append(a)
        a,b = b,b+a

fib(int(input("the upperlimit")))
print(flist)


################## Sirinte code
def fib(ul):
    a,b = 1,2
    flist = [a]
    while a<ul:
        a,b=b,a+b
        flist.append(a)
    return flist

fl = fib(400000)
s = 0
for x in fl:
    if x%2 == 0:
        s+=x
print("Sum:",s)