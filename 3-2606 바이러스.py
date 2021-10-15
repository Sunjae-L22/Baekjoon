# 2606번 바이러스
# BFS, DFS
import sys
from collections import deque
N_of_computer = int(input())
computer_connection = [[0] * (N_of_computer+1) for i in range(N_of_computer+1)]
connected_pair = int(input())

# 컴퓨터가 연결되어있으면 2차원 배열의 값을 1로 변경
for _ in range(connected_pair):
    a, b = map(int, sys.stdin.readline().split())
    computer_connection[a][b] = computer_connection[b][a] = 1


def warm_virus(x):
    infected = [1]
    q = deque()
    q.append(x)
    while q:
        tmp = q.popleft()
        for i in range(1, N_of_computer+1):
            # 얀결되어있으면! infected += 1, q.append
            if computer_connection[tmp][i] == 1 and i not in infected:
                infected.append(i)
                q.append(i)
    print(len(infected)-1)


warm_virus(1)