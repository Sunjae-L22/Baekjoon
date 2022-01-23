# 9095번 1, 2, 3 더하기
# 다이나믹 프로그래밍
import sys
T = int(sys.stdin.readline())
sum_1_2_3 = [0 for i in range(12)]

sum_1_2_3[1] = 1
sum_1_2_3[2] = 2
sum_1_2_3[3] = 4
for i in range(4, 12):
    sum_1_2_3[i] = sum_1_2_3[i-3] + sum_1_2_3[i-2] + sum_1_2_3[i-1]

for i in range(T):
    n = int(sys.stdin.readline())
    print(sum_1_2_3[n])