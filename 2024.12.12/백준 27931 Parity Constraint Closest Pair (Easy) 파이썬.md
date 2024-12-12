```
import sys 

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

INF = float('inf')

last_even = None
last_odd = None

arr.sort()
odd = INF
even = INF
for i in range(len(arr)):
    # 홀수 라면
    if arr[i] % 2:
        if last_even != None:
            odd = min(odd, arr[i] - arr[last_even])
        if last_odd != None:
            even = min(even, arr[i] - arr[last_odd])
        last_odd = i
    # 짝수라면
    else:
        if last_odd != None:
            odd = min(odd, arr[i] - arr[last_odd])
        if last_even != None:
            even = min(even, arr[i] - arr[last_even])
        last_even = i

if even != INF:
    print(even, end = ' ')
else:
    print(-1, end = ' ')
if odd != INF:
    print(odd, end = ' ')
else:
    print(-1, end = ' ')
```

