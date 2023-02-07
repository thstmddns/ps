
#
# def bfs(N, K, temp):
#     if N == K:
#         print(0)
#         return
#     if len(que) == 0 or temp == K:
#         print(total[temp])
#         return
#     else:
#         if que[0] < N:
#             temp = que[0]
#             que.popleft()
#             total[temp] = 1
#             if 0 <= temp * 2 < Max and visited[temp * 2] == 0:
#                 visited[temp * 2] = 1
#                 total[temp * 2] = total[temp] + 1
#                 if temp * 2 not in que:
#                     que.append(temp * 2)
#             else:
#                 if total[temp * 2] > total[temp] + 1:
#                     total[temp * 2] = total[temp] + 1
#                     if temp * 2 not in que:
#                         que.append(temp * 2)
#         elif que[0] > K:
#             temp = que[0]
#             que.popleft()
#
#             if temp - 1 == K:
#                 li.append(total[temp] + 1)
#             elif 0 <= temp - 1 < Max and visited[temp - 1] == 0:
#                 visited[temp - 1] = 1
#                 total[temp - 1] = total[temp] + 1
#                 if temp - 1 not in que:
#                     que.append(temp - 1)
#             else:
#                 if total[temp - 1] > total[temp] + 1:
#                     total[temp - 1] = total[temp] + 1
#                     if temp - 1 not in que:
#                         que.append(temp - 1)
#         else:
#             temp = que[0]
#             que.popleft()
#             if 0 <= temp - 1 < Max and visited[temp - 1] == 0:
#                 visited[temp - 2] = 1
#                 total[temp - 1] = total[temp] + 1
#                 if temp - 1 not in que:
#                     que.append(temp - 1)
#             else:
#                 if total[temp - 1] > total[temp] + 1:
#                     total[temp - 1] = total[temp] + 1
#                     if temp - 1 not in que:
#                         que.append(temp - 1)
#             if 0 <= temp + 1 < Max and visited[temp + 1] == 0:
#                 visited[temp + 1] = 1
#                 total[temp + 1] = total[temp] + 1
#                 if temp + 1 not in que:
#                     que.append(temp + 1)
#             else:
#                 if total[temp + 1] > total[temp] + 1:
#                     total[temp + 1] = total[temp] + 1
#                     if temp + 1 not in que:
#                         que.append(temp + 1)
#             if 0 <= temp * 2 < Max and visited[temp * 2] == 0:
#                 visited[temp * 2] = 1
#                 total[temp * 2] = total[temp] + 1
#                 if temp * 2 not in que:
#                     que.append(temp * 2)
#             else:
#                 if total[temp * 2] > total[temp] + 1:
#                     total[temp * 2] = total[temp] + 1
#                     if temp * 2 not in que:
#                         que.append(temp * 2)
#     bfs(N, K, temp)
#
#
# N, K = map(int, sys.stdin.readline().split())
#
# que = deque()
# que.append(N - 1)
# que.append(N)
# que.append(N + 1)
# que.append(2 * N)
#
# Max = 10 ** 5
# visited = [0] * (Max + 1)
# total = [0] * (Max + 1)
# li = []
#
# bfs(N, K, 0)
import sys
from collections import deque

def bfs():
    que = deque()
    que.append(N)
    while que:
        x = que.popleft()
        if x == K:
            print(total[K])
            break
        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= MAX and not total[i]:
                total[i] = total[x] + 1
                que.append(i)

MAX = 10 ** 5
total = [0] * (MAX + 1)
N, K  = map(int, sys.stdin.readline().split())

bfs()