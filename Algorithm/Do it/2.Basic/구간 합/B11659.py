# 구간 합 구하기 1
"""
문제: 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력: 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 
둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 
셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력: 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

예제 입력 1 
5 3
5 4 3 2 1
1 3
2 4
5 5
예제 출력 1 
12
9
1
"""

# 나의 답
N, M = map(int, input().split())

numbers = list(map(int,input().split()))


sum_numbers = [0]
sum_number = 0

for i in range(N):
  sum_number += numbers[i]
  sum_numbers.append(sum_number)

i1, j1 = map(int, input().split())
result1 = sum_numbers[j1] - sum_numbers[i1-1]

print(result1)

i2, j2 = map(int, input().split())
result2 = sum_numbers[j2] - sum_numbers[i2-1]

print(result2)

i3, j3 = map(int, input().split())
result3 = sum_numbers[j3] - sum_numbers[i3-1]

print(result3)

# 예시 답
import sys # 시간초과 방지
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
  temp = temp + i
  prefix_sum.append(temp)

for i in range(quizNo):
  s, e = map(int, input().split())
  print(prefix_sum[e] - prefix_sum[s-1])