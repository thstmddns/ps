```
import sys
from collections import deque

que_Y = deque('YONSEI')
que_K = deque('KOREA')

S = sys.stdin.readline().rstrip()

for i in S:
    if i == que_Y[0] or i == que_K[0]:
        if i == que_Y[0]:
            que_Y.popleft()
        if i == que_K[0]:
            que_K.popleft()
    if len(que_K) == 0 or len(que_Y) == 0:
        if len(que_Y) == 0:
            print('YONSEI')
            break
        elif len(que_K) == 0:
            print('KOREA')
            break
```