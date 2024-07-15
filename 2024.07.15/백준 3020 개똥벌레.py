$$

$$

```
import sys

N, H = map(int, sys.stdin.readline().split())
h = [0] * H 
for i in range(N):
    s = int(sys.stdin.readline())
    if i % 2 == 0:
        h[H - s] += 1
        
    else:   
        h[s] -= 1
        h[0] += 1
for j in range(1, H):
    h[j] += h[j - 1]
min_v = min(h)
count_min_v = h.count(min_v)
print(min_v, count_min_v)
```

