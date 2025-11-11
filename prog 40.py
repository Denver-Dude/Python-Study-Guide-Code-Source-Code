inp = input("Enter two intergers")
a,b = inp.split()
n,m = int(a),int(b)
print(n,m,n+m,n-m,m*n,m//n)

#FORMATING


print("%d %d %d %d %d %d"%(n,m,n+m,n-m,m*n,m//n))
#d is used when we need it as integers


print("%6d %6d %6d %6d %6d %6d"%(n,m,n+m,n-m,m*n,m//n))
#Now we can use space with 6


print("%6f %6f %6f %6f %6f %6f"%(n,m,n+m,n-m,m*n,m//n))
#f is used for deicmals


print("%6f %6f %6f %6f %6f %6.2f"%(n,m,n+m,n-m,m*n,m//n))
#f.(number will show much decimals it has to produce) is used for deicmals


print("{} {} {} {} {} {}".format(n,m,n+m,n-m,m*n,m//n))
#{} will do partition like eariler


print("{1} {2} {3} {4} {5} {6}".format(n,m,n+m,n-m,m*n,m//n))
#{adding numbers will have index} will do partition like eariler
#rearranging the numbers will keep them in different order



print("{1:6d} {2:6d} {3:6d} {4:6d} {5:6.2f} {6:6d}".format(n,m,n+m,n-m,m*n,m//n))
#formating with all the properties we used


print("a:{0} b:{1} sum:{2} product{4:6d}".format(n,m,n+m,n-m,m*n,m//n))
#Now printing with text inside the product