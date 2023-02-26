```
import sys

def check(idx):
    for i in range(idx):
        if row[i] == row[idx] or abs(row[idx] - row[i]) == idx - i:
            return False
    return True

def dfs(idx):
    global result

    if idx == N:
        result += 1
    else:
        for i in range(N):
            row[idx] = i
            if check(idx):
                dfs(idx + 1)

N = int(sys.stdin.readline())

cnt = 0

result = 0
row = [0] * N
dfs(0)
print(result)
```