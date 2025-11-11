#Quesitons Solved

#20. Given a string S, print a new string containing only distinct characters from S.
s = "successful"
res = ""
for c in s:
    if c not in res:
        res += c
print(res)

#21. Given a string S, print the number of vowels of each type in S.
s = "education"
vowels = "aeiou"
for v in vowels:
    print(v, ":", s.count(v))

#22. Write a function which takes a string as input and returns letter frequency as a dictionary.
#23. Write a function which returns True if a given number is perfect and False otherwise.
def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False

print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(10))

#24. Write a function to find the Pythagorean triple which adds to 1000.
#27. Write a function to generate a Collatz sequence. Now print the starting number less than one million which will produce the longest chain.
