import sys
input = sys.stdin.readline

s = list(input().rstrip())
p = list(input().rstrip())

pi = [0]*len(p)


def makePi(p):
  j = 0
  for i in range(1, len(p)):
    while j > 0 and p[i] != p[j]:
      j = pi[j - 1]
    if p[i] == p[j]:
      j += 1
      pi[i] = j


def kmp(s, p):
  makePi(p)
  j = 0
  for i in range(len(s)):

    while j > 0 and s[i] != p[j]:
      j = pi[j-1]

    if s[i] == p[j]:
      if j == len(p) - 1:  # 끝까지 확인
        print(1)
        return
      else:  # 아직 뒤에 남음
        j += 1

  print(0)
  return


kmp(s, p)

# 문자열의 길이기 100만으로 매우 길다 -> 단순히 비교하면 시간초과
# 건너뛰는 걸 생각하고 틀렸을때 앞의 맞은부분은 무시하고 그부분부터 검사했으나 실패
# -> 반례: s - abababc p - ababc
# KMP가 단순히 건너뛰는 것이 아니라 접두사와 접미사 테이블을 만들고 확실히 건너뛸 수 있는 부분만 확인해야함
