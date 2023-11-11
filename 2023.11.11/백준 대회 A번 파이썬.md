```python
import sys

N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())
if N > 2:
    if s == 'annyong':
        if k % 2 == 0:
            if 1 < k < 3:
                print(3)
            elif k == 1:
                print(1)
            else:
                print(k - 1)
        else:
            print(k)
    else:
        if k % 2:
            if k < 4:
                print(2)
            else:
                print(k - 1)
        else:
            print(k)
else:
    if s == 'annyong':
        print(1)
    else:
        print(2)
```