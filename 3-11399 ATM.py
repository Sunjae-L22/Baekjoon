# 11399번 ATM
# 그리디 알고리즘, 정렬

import sys
N = int(sys.stdin.readline())
P_i = list(map(int, sys.stdin.readline().split()))

# 시간이 조금 걸리는 순으로 정렬(오름차순)
P_i.sort()

tot_time = 0
for i in range(N):
    tot_time += (P_i[i] * (N-i))

print(tot_time)