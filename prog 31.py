# given a string print the number of vowels in the string
string = input("Input Of The Word")
vowels = "aeiou"
count = sum(1 for char in string if char in vowels)
print("Number of vowels:", count)