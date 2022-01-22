import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))

ans = n+1
l, r = 0, 0
temp = 0

while True:
  if temp >= s:
    ans = min(ans, r-l)
    temp -= num[l]
    l += 1
  elif r == n:
    break
  else:
    temp += num[r]
    r += 1


print(ans if ans != n+1 else 0)

# 투포인터 문제
# 처음엔 LIS 문제처럼 dp로 접근하였으나 n제곱의 복잡도로 해결불가
# 왼쪽가 오른쪽을 가리키는 포인터로 선형시간안에 풀이 가능