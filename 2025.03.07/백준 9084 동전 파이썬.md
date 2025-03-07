```
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    price = int(sys.stdin.readline())
    dp = [[0] * (price + 1) for _ in range(N + 1)]
    for c in range(N + 1):
        dp[c][0] = 1

    for i in range(1, price + 1):
        for j in range(1, N + 1):
            dp[j][i] = dp[j - 1][i]

            if i - coin[j - 1] >= 0:
                dp[j][i] += dp[j][i - coin[j - 1]]
    print(dp[N][price])
```

