```
import sys

li = sorted([int(sys.stdin.readline().strip()) for i in range(3)])
print(li[len(li) // 2])
```