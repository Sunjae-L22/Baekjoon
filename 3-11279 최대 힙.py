# 11279번 최대 힙
# 자료 구조 - 우선순위 큐

import sys
import heapq
N = int(sys.stdin.readline())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(-1 * result)