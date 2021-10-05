N = int(input())

div = 5
n_5 = 0

while N >= div:
    n_5 += N // div
    div *= 5

print(n_5)