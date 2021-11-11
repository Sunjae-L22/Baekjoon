# 5525번 IOIOI
# 문자열
import sys
N = int(input())  # O의 개수
M = int(input())  # 문자열의 길이
S = sys.stdin.readline()       # 문자열

num_0 = 0
num_pn = 0
i = 1

while i < M-1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        num_0 += 1
        if num_0 == N:
            num_pn += 1
            num_0 -= 1
        i += 1
    else:
        num_0 = 0
    i += 1
print(num_pn)