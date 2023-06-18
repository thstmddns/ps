```
for` `t in range(1, 11):
  ``N = ``int``(input())
  ``h = list(map(``int``, input().split()))
  ``h_cnt = 0
  ``around = [-2, -1 , 1, 2]
  ``for` `i in range(2, N - 2):
    ``max_h = 0
    ``for` `j in around:
      ``if` `h[i + j] > max_h:
        ``max_h = h[i + j]
    ``if` `h[i] > max_h:
      ``h_cnt += h[i] - max_h
  ``print(f``'#{t} {h_cnt}'``)
```