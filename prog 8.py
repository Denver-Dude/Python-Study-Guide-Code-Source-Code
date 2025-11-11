def add(Num1,Num2):
    Num1 = int(Num1)
    Num2 = int(Num2)
    return Num1+Num2

inp = input("Enter Two Integers: ")
a,b = inp.split()
p,q = int(a), int(b)
print(add(p,q))
