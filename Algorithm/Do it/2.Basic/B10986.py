# 나머지 합 구하기
"""
문제 : 
수 N개 A1, A2, ..., AN이 주어진다. 
이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

입력 :
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력 :
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

예제 입력1 :
5 3
1 2 3 1 2

예제 출력1 :
7

# 내 답
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

prefix = 0
D = []
for i in A:
  prefix += i
  D.append(prefix)

C =[0] * M
result = 0

for i in range(N):
  remainder = D[i] % M
  if remainder == 0:
    result += 1
  C[remainder] += 1

for i in C:
  if i > 1:
    result += (i * (i-1))//2
print(result)

# 예시 답안
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1,n):
  S[i] = S[i-1] + A[i]

for i in range(n):
  remainder = S[i] % m
  if remainder == 0:
    answer += 1
  C[remainder] += 1

for i in range(m):
  if(C[i] > 1):
    answer += (C[i] * (C[i] - 1)//2)
    
print(answer)