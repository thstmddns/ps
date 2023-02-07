import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
find = deque(list(map(int, sys.stdin.readline().split())))

arr = [i for i in range(1, N + 1)]
que = deque(arr)

cnt = 0
while find:
    if find[0] == que[0]:
        que.popleft()
        find.popleft()
    elif que.index(find[0]) < len(que) / 2:
        while find[0] != que[0]:
            que.append(que[0])
            que.popleft()
            cnt += 1
    else:
        while find[0] != que[0]:
            que.appendleft(que[-1])
            que.pop()
            cnt += 1
print(cnt)