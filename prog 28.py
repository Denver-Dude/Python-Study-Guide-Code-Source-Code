#clousure
def outer(a):
    def inner(b):
        return a+b
    return inner

f1=outer(100)
f2=outer(200)

print(f1(10))


print(f2(10))

# this is a variable that stores the function
#the state of the variables