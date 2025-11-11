a = range(1,11)
print(a)
#it returns a function object

#IF list is waht is needed

a = list(range(1,11))
print(a)

#--- tuple --- #
b = tuple(range(1,11))
print(b)

print(a[::-1])# list is reversed
print(b[::-1])# zTuple is reversed

#what we cannot do with tuple

#list is mroe convinet
#tuple is a stricter data structure
#you can modify elements in list and not in tuple
a[5] = 100
print(a)#5th eleemetn becomes 100

#trying with tuple
b[5]= 100
print(b)#this will not work for tuple




#when we return from a function, it returns in tuple as that is more safer
