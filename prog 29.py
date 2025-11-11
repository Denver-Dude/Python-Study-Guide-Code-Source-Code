s = 0
for x in range(101):
    if x%2==0:
        s+=x
print("Sum",s)

########## List comphresnion
print(sum([x for x in range(101)if x%2==0]))