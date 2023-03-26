```
import sys

vote = sys.stdin.readline().rstrip()

cnt_uc = 0
cnt_dp = 0

for i in vote:
    if i == 'U':
        cnt_uc += 1
    elif i == 'C':
        cnt_uc += 1
    elif i == 'D':
        cnt_dp += 1
    elif i == 'P':
        cnt_dp += 1
if (cnt_uc == 0 and cnt_dp == 0):
    print('C')
elif cnt_uc == 1 and cnt_dp == 1:
    print('DP')
elif cnt_dp == 0 and cnt_uc != 0:
    print('U')
elif cnt_dp != 0 and cnt_uc == 0:
    print('DP')
elif cnt_dp > cnt_uc:
    print('DP')
elif cnt_dp <= cnt_uc:
    print('UDP')
```

이 문제는 틀렸다. 그래서 위와 같이 수정했는데 시간이 오버돼서 제출하지 못했다