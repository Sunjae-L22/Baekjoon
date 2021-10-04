import sys
N, M = map(int, sys.stdin.readline().split())

dictionary = {}

for i in range(1, N+1):
    a = input().rstrip()
    dictionary[i] = a
    dictionary[a] = i

for j in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(dictionary[int(question)])
    else:
        print(dictionary[question])