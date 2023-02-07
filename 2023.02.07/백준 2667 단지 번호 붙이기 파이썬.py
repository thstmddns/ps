```
from collections import deque

def bfs():
    ccnt = 0
    while queue:
        q = queue.popleft()
        for k in range(4):
            ni = q[0] + dr[k]
            nj = q[1] + dc[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                queue.append([ni, nj])
                ccnt += 1
    if ccnt == 0:
        ccnt = 1
    li.append(ccnt)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

queue = deque()
li =[]
cnt = 0


for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            queue.append([i, j])
            bfs()

li.sort()
print(cnt)
for i in range(cnt):
    print(li[i])
```