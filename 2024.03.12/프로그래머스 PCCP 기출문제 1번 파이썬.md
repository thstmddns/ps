```
from collections import deque
def solution(bandage, health, attacks):
    dp = [0] * max(attacks[-1][0] + 1, len(bandage))
    dp[0] = health
    count = 0
    answer = 0
    for i in range(1, len(dp)):
        if dp[i - 1] <= 0:
            break
        for j in attacks:
            if i == j[0]:
                dp[i] = dp[i - 1] - j[1]
                count = 0
                if dp[i] <= 0:
                    answer = -1
                break
        else:
            dp[i] = dp[i - 1] + bandage[1]
            count += 1
            if count == bandage[0]:
                dp[i] += bandage[2]
                count = 0
            if dp[i] > health:
                dp[i] = health

    if answer != -1:
        answer = dp[-1]
    return answer
```

