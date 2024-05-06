```
import sys

a, b, c = map(int, sys.stdin.readline().strip().split())
res = 0
if a == 0:
    res = int((c ** 2 - b))
elif b == 0:
    res = int((c ** 2 - a))
else:
    res = int((a + b) ** 0.5)
print(res)
```