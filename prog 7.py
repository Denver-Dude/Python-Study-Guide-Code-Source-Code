# Print the sum of all numbers less than 1000, which are multiples of 3 or 5
sum_multiples = 0

for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        sum_multiples += i

print(sum_multiples)


