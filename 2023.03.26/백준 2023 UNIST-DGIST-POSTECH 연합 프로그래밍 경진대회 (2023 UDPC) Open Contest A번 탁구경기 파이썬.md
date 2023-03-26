```
import sys

N = int(sys.stdin.readline())
cnt_P = 0
cnt_D = 0
for i in range(N):
    result = sys.stdin.readline().rstrip()
    if result == 'D':
        cnt_D += 1
    else:
        cnt_P += 1
    if cnt_P - cnt_D <= - 2 or cnt_P - cnt_D >= 2:
        break
print(f'{cnt_D}:{cnt_P}')
```

이 문제는 굉장히 쉽게 풀어다 백준 기준으로 브론즈 4~5 정도 일듯