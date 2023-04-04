```
import sys

total = 0
while True:
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    if len(arr) == 0:
        break
    if arr[0] == 'Es':
        total += int(arr[1]) * 21
    elif arr[0] == 'Stair':
        total += int(arr[1]) * 17

if total == 5096:
    print(5096)
else:
    print(total)
```