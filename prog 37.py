
L = [1, 2, 3, 4, 5]
n = 2

if n < 0:
    n = abs(n)
    L = L[n:] + L[:n]
else:
    n = n % len(L)
    L = L[-n:] + L[:-n]

print(L)
