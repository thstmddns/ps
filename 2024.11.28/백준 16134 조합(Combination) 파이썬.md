```
import sys

N, R = map(int, sys.stdin.readline().strip().split())
p = 1_000_000_007

# 분자 산출
son = 1
for s in range(N - R + 1, N + 1):
    son = (son * s) % p 

# 분모 계산
mother = 1
for m in range(1, R + 1):
    mother = (mother * m) % p
    
# 폐르마 소정리를 활용한 분모의 역원 구하기
z = p - 2
answer = 1
result = 1
while z > 0:
    if z % 2 == 1:
        result = (result * mother) % p
    mother = (mother  * mother) % p
    z //= 2

print(son * result % p)
```

