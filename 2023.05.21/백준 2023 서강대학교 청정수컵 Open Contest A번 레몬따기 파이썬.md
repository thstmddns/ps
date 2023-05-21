```
import sys

N = int(sys.stdin.readline())
tree = list(map(int, sys.stdin.readline().split()))
dp = [0] * N
dp[0] = tree[0]
if len(tree) == 0:
    print(tree[0] - 1)
else:
    for i in range(1, N):
        if tree[i] > dp[i - 1] - 1:
            dp[i] = tree[i]
        else:
            dp[i] = dp[i - 1] - 1
    print(dp[-1] - 1)
```