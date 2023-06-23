### 첫번째 풀이

```
for tc in range(1, 11):
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    total = 0
    for i in range(n):
        for j in range(n):
            if len(stack) == 0 and mag[j][i] == 2:
                continue
            elif len(stack) != 0 and mag[j][i] == 2:
                stack.append(mag[j][i])
            elif mag[j][i] == 1:
                stack.append(mag[j][i])
        while len(stack) != 0 and stack[-1] == 1:
            stack.pop()
        flag = 0
        while len(stack) != 0:
            if stack[-1] != flag:
                total += 1
                flag = stack.pop()
            else:
                stack.pop()
    answer = int(total * 0.5)
    print(f'#{tc} {answer}')
```

### 두번째 풀이

```
for` `tc in range(1, 11):
  ``n = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(n)]
  ``stack = []
  ``total = 0
  ``for` `i in range(n):
    ``for` `j in range(n):
      ``if` `len(stack) == 0 and mag[j][i] == 2:
        ``continue
      ``elif len(stack) != 0 and mag[j][i] == 2:
        ``stack.append(mag[j][i])
      ``elif mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `len(stack) != 0 and stack[-1] == 1:
      ``stack.pop()
    ``flag = 0
    ``while` `len(stack) != 0:
      ``if` `stack[-1] != flag:
        ``total += 1
        ``flag = stack.pop()
      ``else``:
        ``stack.pop()
  ``print(f``'#{tc} {int(total * 0.5)}'``)
```

### 세번째 풀이

```
for` `tc in range(1, 11):
  ``n = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(n)]
  ``stack = []
  ``total = 0
  ``for` `i in range(n):
    ``for` `j in range(n):
      ``if` `len(stack) != 0 and mag[j][i] == 2:
        ``stack.append(mag[j][i])
      ``elif mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `len(stack) != 0 and stack[-1] == 1:
      ``stack.pop()
    ``flag = 0
    ``while` `len(stack) != 0:
      ``if` `stack[-1] != flag:
        ``total += 1
        ``flag = stack.pop()
      ``else``:
        ``stack.pop()
  ``print(f``'#{tc} {int(total * 0.5)}'``)
```

### 네번째 풀이

```
for` `tc in range(1, 11):
  ``n = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(n)]
  ``stack = []
  ``total = 0
  ``for` `i in range(n):
    ``for` `j in range(n):
      ``if` `len(stack) == 0 and mag[j][i] == 2:
        ``continue
      ``elif len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `len(stack) != 0 and stack[-1] == 1:
      ``stack.pop()
    ``flag = 0
    ``while` `len(stack) != 0:
      ``if` `stack[-1] != flag:
        ``total += 1
        ``flag = stack.pop()
      ``else``:
        ``stack.pop()
  ``print(f``'#{tc} {int(total * 0.5)}'``)
```

### 다섯번째 풀이

```
for` `tc in range(1, 11):
  ``n = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(n)]
  ``stack = []
  ``t = 0
  ``for` `i in range(n):
    ``for` `j in range(n):
      ``if` `len(stack) == 0 and mag[j][i] == 2:
        ``continue
      ``elif len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 여섯번째 풀이

```
for` `tc in range(1, 11):
  ``n = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(n)]
  ``stack = []
  ``t = 0
  ``for` `i in range(n):
    ``for` `j in range(n):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 일곱번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(input().split()) ``for` `_ in range(N)]
  ``stack = []
  ``t = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == ``'2'` `or mag[j][i] == ``'1'``:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == ``'1'``:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 여덟번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(input().split()) ``for` `_ in range(N)]
  ``stack = []
  ``t = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == ``'2'` `or mag[j][i] == ``'1'``:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == ``'1'``:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 아홉번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(input().split()) ``for` `_ in range(N)]
  ``stack = []
  ``t = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == ``'2'` `or mag[j][i] == ``'1'``:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == ``'1'``:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {t//2}'``)
```

### 열번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``stack = []
  ``t = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 열한번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``stack = []
  ``t = f = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 열두번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``stack = []
  ``t = f = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 열세번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``stack = []
  ``t = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``f = 0
    ``while` `len(stack):
      ``if` `stack[-1] != f:
        ``t += 1
      ``f = stack.pop()
  ``print(f``'#{tc} {int(t * 0.5)}'``)
```

### 열네번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``stack = []
  ``total = 0
  ``for` `i in range(N):
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``flag = 0
    ``while` `len(stack):
      ``if` `stack[-1] != flag:
        ``total += 0.5
      ``flag = stack.pop()
  ``print(f``'#{tc} {int(total)}'``)
```

### 열다섯번째 풀이

```
for` `tc in range(1, 11):
  ``N = ``int``(input())
  ``mag = [list(map(``int``, input().split())) ``for` `_ in range(N)]
  ``total = 0
  ``for` `i in range(N):
    ``stack = []
    ``for` `j in range(N):
      ``if` `len(stack) != 0 and mag[j][i] == 2 or mag[j][i] == 1:
        ``stack.append(mag[j][i])
    ``while` `stack[-1] == 1:
      ``stack.pop()
    ``flag = 0
    ``for` `k in stack:
      ``if` `k != flag:
        ``total += 0.5
        ``flag = k
  ``print(f``'#{tc} {int(total)}'``)
```



1. 총평
   1. 보시다시피 코드를 조금씩 수정하면서 돌려보았다. 시간복잡도 면에선 일곱번째, 열다섯번째가 189ms로 가장 우수했고, 공간복잡도 면에선 열다섯번째가 60,500kb으로 가장 우수했다. 아마 스택의 pop 연산을 하지 않아서 인것 같다.