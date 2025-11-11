num =[]
for x in range(1,11):
    num.append(x)
print(num)

letters =list('abcdedfeadsasidjoad')
print(letters) #now it saves the entire string as induvidila character elements
letters1=[1]


#does the same thing
for c in range 'abcdefghijklmnopqrstuvwxyz':
    letters1.append(c)
print(letters1)


print(list(zip(list('abcde'), list(range(1,6)))))
#the abcde is made into a list, it has values from 1 to 5, so what it does is, it takes first element of first element then take 1st from the other function, then makes a tuple, likewise keeps on making it.
print(dict(zip(list('abcde'), list(range(1,6)))))#this is a dictionary now

#this is a tuple
print(tuple(zip(list('abcde'), list(range(1,6)))))
