# 1931번 회의실 배정
# 그리디 알고리즘
import sys
N = int(input())
# 회의실 이용 시간을 2차원 배열에 입력
time = [[0] * 2 for _ in range(N)]
for i in range(N):
    time[i][0], time[i][1] = map(int, sys.stdin.readline().split())

# 매번 종료 시간이 가장 빠른 정보를 골라야 함
# 2차원 배열을 2열(회의 종료 시간) 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))
conference = 0
end = 0

for i in range(N):
    if time[i][0] >= end:
        conference += 1
        end = time[i][1]

print(conference)