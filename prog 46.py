def outer_parm(l1,l2):
    def outer(fun):
        def inner(p,q):
            if p<l1: p = l1
            if p>12: p = l2
            if p<l1: q = l1
            if q>l2: q=l2
            return fun(p,q)
        return inner()
    return outer()

@outer_parm(400,600):
def add(a,b)
    return a+b

print(add(420,520))
print(add(-120,520))
print(add(650,420))
print(add(420,-120))
print(add(420,650))
