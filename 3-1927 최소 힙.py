# 1927번 최소 힙
# 자료구조, 우선순위 큐
import heapq as h
import sys
N = int(input())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    # 자연수면 배열에 x를 추가하는 연산
    if x > 0:
        h.heappush(heap, x)
    # 0이면 가장 작은 값을 출력하고 그 값을 배열에서 제거
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(h.heappop(heap))