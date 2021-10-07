# 1764번 듣보잡
# 해시를 사용한 집합
import sys
N, M = map(int, sys.stdin.readline().split())
no_listen = {}
no_see = {}

for i in range(N):
    no_listen[input().rstrip()] = i

for j in range(M):
    no_see[input().rstrip()] = j

dbj = []
for name in no_listen:
    if name in no_see:
        dbj.append(name)

dbj.sort()
print(len(dbj))
for name in dbj:
    print(name, sep='\n')