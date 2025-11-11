def fib(ul):
    a,b = 1,2
    yield a
    while a<ul:
        a,b=b,a+b
        yield a
    return

s = 0
for x in fib(400000000):
    if x%2==0:
        s+=x
print("sum:",s)