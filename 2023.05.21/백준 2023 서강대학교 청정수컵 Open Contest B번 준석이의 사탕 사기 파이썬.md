```
import sys

N = int(sys.stdin.readline())
candy = list(map(int, sys.stdin.readline().split()))
if len(candy) == 1 and candy[0] % 2 == 1:
    print(0)
else:
    li = []
    total = 0
    for i in candy:
        if i % 2 == 1:
            li.append(i)
            total += i
        else:
            total += i
    if len(li) % 2 == 1:
        total -= min(li)
    print(total)
```