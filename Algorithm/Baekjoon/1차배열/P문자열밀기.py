# 문자열 밀기
"""
문제 : 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 
마지막 문자는 맨 앞으로 이동시키면 "ohell"이 됩니다. 
이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때, 
A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 return하고 
밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

입출력 예
A	B	result
"hello"	"ohell"	1
"apple"	"elppa"	-1
"atat"	"tata"	1
"abc"	"abc"	0

"""

# 나의 답
def solution(A,B) :
  for cnt in range(len(A)) :
    if A == B :
      return cnt
    A = A[-1] + A[:-1]
    print("A[-1] :",A[-1])
    print("A[:-1] :",A[:-1])
  return -1

print(solution("hello","ohell"))
print(solution("hello","elloh"))
print(solution("apple","elppa"))
print(solution("atat","tata"))
print(solution("abc","abc"))
