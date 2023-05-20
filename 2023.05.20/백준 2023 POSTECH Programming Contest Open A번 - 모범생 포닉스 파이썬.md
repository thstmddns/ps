```
import sys
N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))
if len(time) == 1:
    print(time[0] // 24, end=' ')
    print(time[0] % 24)
else:
    s = sum(time) + (len(time) - 1) * 8
    print(s // 24, end=' ')
    print(s % 24)
```

+ 백준 대회 문제입니다.