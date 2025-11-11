def is_palindrome(st):
    return st == st[::-1]#this is a boolean expression which is evaluated, if it is true then return
#this shows true or false

st = input("Enter A string")
if is_palindrome(st):
    print(st,"is a palindrome")
else:
    print(st,"is not a palindrome")
