inp = input("enter two integers and an arithmetic syumbol : ")
a,c,b = inp.split()
a= int(a)
b=int(b)
if c == "+":
    print("Sum=",a+b)
elif c == "-":
    print("difference=",a-b)
elif c == "*":
    print("product=",a*b)
elif c == "/":
    print("floating point quotient=",a/b)
elif c == "//":
    print("integer quotient=",a//b)
elif c == "%":
    print("reminder=",a%b)
elif c == "**":
    print("expontent=",a**b)
else:
    print("Invalid Operation")
