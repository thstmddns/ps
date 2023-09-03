```
import sys

y = int(sys.stdin.readline())
m = int(sys.stdin.readline())
print(m + m - y)
```

### 성능 요약

메모리:   31256KB, 시간:40ms 

(23.09.03 기준 시간 복잡도 순위 :2818/6182)



### 나의 풀이

1. 단순한 사칙연산



### 분류

- [수학](https://www.acmicpc.net/problem/tag/124)
- [구현](https://www.acmicpc.net/problem/tag/102)

### 문제 설명

1. You know a family with three children. Their ages form an arithmetic sequence: the difference in ages between the middle child and youngest child is the same as the difference in ages between the oldest child and the middle child. For example, their ages could be 5, 10 and 15, since both adjacent pairs have a difference of 5 years.

   Given the ages of the youngest and middle children, what is the age of the oldest child?


### 입력

The input consists of two integers, each on a separate line. The first line is the age Y of the youngest child (0 ≤ Y ≤ 50). The second line is the age M of the middle child (Y ≤ M ≤ 50).

### 출력

The output will be the age of the oldest child.