import sys
from collections import deque

def bfs():
    while que:
        q = que.popleft()
        if q[0] == N - 1 and q[1] == M - 1:
            print(total[q[0]][q[1]])
            return
        for i in range(4):
            ni = q[0] + dr[i]
            nj = q[1] + dc[i]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                total[ni][nj] += total[q[0]][q[1]]
                visited[ni][nj] = 1
                que.append([ni, nj])


N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, input())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

que = deque()
que.append([0, 0])

total = [[1] * (M) for _ in range(N)]
visited = [[0] * (M) for _ in range(N)]

bfs()
