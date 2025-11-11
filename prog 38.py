import random

# Generate a random list of 20 numbers between 1 and 10
r = [random.randint(1, 10) for _ in range(20)]
print(r)


def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

largest = find_largest(r)
print("Largest number:", largest)


second_largest = 0
for num in r:
    if num != largest:
        if second_largest is 0 or num > second_largest:
            second_largest = num

print("Second largest number:", second_largest)
