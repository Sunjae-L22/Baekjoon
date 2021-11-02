# 5430번 AC
# 구현, 자료구조, 문자열, 파싱, 덱
import sys
from collections import deque
T = int(input())


def AC(P, N, NUMS):
    rev = 0
    if P.count('D') > N:
        return 'error'
    else:
        for func in P:
            if func == 'R':
                rev += 1
            elif func == 'D':
                if rev % 2 == 0:
                    NUMS.popleft()
                else:
                    NUMS.pop()
        if rev % 2 == 1:
            NUMS.reverse()
        return '[' + ','.join(NUMS) + ']'


for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    nums = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    print(AC(p, n, nums))