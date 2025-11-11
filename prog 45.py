def outer(fun):
    def inner(p,q):
        if p<100: p = 100
        if p>200 : p =200
        if q<100: q = 100
        if q>200: q=200
        return fun(p,q)
    return inner



#this can be written as
@outer #add fuction is decorated with add
#decorators
def add(a,b):
    return a+b
print(add(120,190))
print(add(-120,190))
print(add(250,190))
print(add(120,-120))
print(add(120,250))
