inp = input("enter two integers")
a,b = inp.split()
m,n = int(a), int(b)
print("Sum:{}".format(m+n))

#EXCEPTION HANDELING
try:
    inp = input("enter two integers")
    a,b = inp.split()
    m,n = int(a), int(b)
    print("Sum:{}".format(m+n))
except:
    print("invalid operation")


#trying different error exceptions from python.org
try:
    inp = input("enter two integers")
    a,b = inp.split()
    m,n = int(a), int(b)
    print("Sum:{}".format(m+n))
except ValueError:#due to some error

    print("invalid operation")
except ZeroDivisionError:
    print("denominator is zero")
finally:
    print("this will always come, even if there is an error or not")


data = input("Enter 2 integers ")
try:
    a,b = data.split()
    m,n = int(a), int(b)
    if m<= 0 or n <= 0:
        fmt = "{} {} {} negative integers are not allowed".format(n,m)
        raise Exception(fmt)

except ValueError:
    print("Nere olle number tha da makryi")
except Exception as ex:
    print(ex)
else:
    print("quotient:",m//n)




#handeling exception as functions

def divide(data):
    data = input("Enter 2 integers ")
    try:
        a, b = data.split()
        m, n = int(a), int(b)
        if m <= 0 or n <= 0:
            fmt = "{} {} {} negative integers are not allowed".format(n, m)
            raise Exception(fmt)

    except ValueError:
        print("Nere olle number tha da makryi")
    except Exception as ex:
        print(ex)
    else:
        print("quotient:", m // n)




