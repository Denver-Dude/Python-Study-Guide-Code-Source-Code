

#SLICESS
#works with tuples, lists and string
#in string we cannot item assign (we cannot change one character with index)



st = 'abcdefghijklmnopqrstuvwxyz'
print(st[10])#prints K from indexing
print(st[-10])#counts from right to left(starts with -1)
print(st[2:5])#prints from 2nd character till 4th character (5th not inculded)
print(st[2:15:2])#prints from 2nd to 14th and skips 2 steps

print(st[10:])#prints from 10th character
print(st[10::2])#prints from 10th character and skips 2 steps
print(st[:10])#prints till the 10th character but not the 10th character

print(st[:10:2])#



print(st[-10:-2])#larger  number should come on the left hand side
print(st[::-1])#it assumes that it has to be printed from right hand side
