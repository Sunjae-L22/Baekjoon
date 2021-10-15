# 2579번 계단 오르기
# 다이나믹 프로그래밍
import sys
N = int(input())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
score = 0

# 마지막 계단을 반드시 밟아야 하므로 그 전에 밟을 수 있는 계단은 N-1 or N-2
# 각 칸까지의 최댓값을 저장하는 리스트 : max_score, 자세한 건 그림 참조
if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[0] + stairs[1])
elif N == 3:
    print(max(stairs[0], stairs[1]) + stairs[2])
else:
    max_score = [0] * N
    max_score[0] = stairs[0]
    max_score[1] = stairs[0] + stairs[1]
    max_score[2] = max(stairs[0], stairs[1]) + stairs[2]
    for i in range(3, N):
        max_score[i] = max(stairs[i - 1] + max_score[i - 3], max_score[i - 2]) + stairs[i]

    print(max_score[N - 1])