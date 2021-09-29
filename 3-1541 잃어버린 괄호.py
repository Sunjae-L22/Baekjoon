import sys
expression = sys.stdin.readline().split('-')

num = []

for i in expression:
    n = 0
    numbers = i.split('+')
    for j in numbers:
        n += int(j)
    num.append(n)

answer = num[0]
for i in range(1, len(num)):
    answer -= num[i]

print(answer)
