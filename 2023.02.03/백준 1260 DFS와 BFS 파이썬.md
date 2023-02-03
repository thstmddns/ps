```
import sys
from collections import deque

def dfs(V, N):
    V = stack[-1]
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited[i] == 1:
            graph[V][i] = graph[i][V] = 0
            visited[i] = 0
            stack.append(i)
            stack1.append(i)
            dfs(V, N)
            stack.pop()
    return stack1

def bfs(V, N):
    if que:
        V = que[0]
        que.popleft()
        for j in range(N + 1):
            if graph1[V][j] == 1 and visited1[j] == 1:
                graph1[V][j] = graph1[j][V] =0
                visited1[j] = 0
                que.append(j)
                queue.append(j)
            if j == N:
                bfs(V, N)
                return queue
    else:
        return queue


N, M, V = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
graph1 = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1
    graph1[a][b] = graph1[b][a] = 1

stack = []
stack1 = []
visited = [1] * (N + 1)

que = deque()
queue = []
visited1 = [1] * (N + 1)

stack.append(V)
stack1.append(V)
visited[V] = 0

que.append(V)
queue.append(V)
visited1[V] = 0


print(*dfs(V, N))
print(*bfs(V, N))
```