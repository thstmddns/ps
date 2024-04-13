```
import sys

while True:
    sum = 0
    N = int(sys.stdin.readline().rstrip())
    if not N:
        break
    for i in range(1, N + 1):
        sum += i
    print(sum)
```