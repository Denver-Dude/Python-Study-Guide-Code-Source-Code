def add(a,b=100):
    c = a+b
    return c
inp = input("enter 2 int")
a,b = inp.split()
p,q = int(a),int(b)
print(add(p,q))
