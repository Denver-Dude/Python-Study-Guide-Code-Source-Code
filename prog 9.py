inp = input("enter two integers & a symbol : ")
Num1,Sign,Num2 = inp.split()
Num1= int(Num1)
Num2=int(Num2)



def Calculator(Num1,Num2,Sign):
    if Sign == "+":
        return "Sum = ", Num1+Num2
    elif Sign == "-":
        return "difference=",Num1 + Num2
    elif Sign == "*":
        return("product=",Num1*Num2)
    elif Sign == "/":
        return("floNum1ting point quotient=",Num1/Num2)
    elif Sign == "//":
        return("integer quotient=",Num1//Num2)
    elif Sign == "%":
        return("reminder=",Num1%Num2)
    elif Sign == "**":
        return("expontent=",Num1**Num2)
    else:
        return("Invalid Operation")
print(Calculator(Num1, Num2, Sign))
