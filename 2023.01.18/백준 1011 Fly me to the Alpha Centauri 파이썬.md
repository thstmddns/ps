```
T = int(input())
for _ in range(1, T + 1):
    X, Y = map(int, input().split())
    distant = Y - X

    k = int(((-1) + (1 + 4 * distant) ** (1/2)) / 2)  # 근의 공식을 이용한 풀이
    remain = distant - (k * (k + 1))  # 남은 거리
    operation = 2 * k    # 작동 횟수

    if 0 < remain <= k + 1:
        operation += 1

    elif remain > k + 1:
        operation += 2


    print(operation)
```