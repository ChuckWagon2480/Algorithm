import sys
input = sys.stdin.readline

INF = 9876543210

n, m = map(int, input().split())
num = [int(input()) for _ in range(n)]

dp = [[INF]*(n+1) for _ in range(n+1)]
# 행 i번째 줄에
# 열 j번째 수까지 입력했을때

if n == 1:
  print((m-num[0])**2)

remain = m
for j in range(1, n+1):
  remain -= num[j-1]
  if remain >= 0:
    dp[1][j] = remain**2
  else:
    break
  remain -= 1

for i in range(2, n+1):
  k = i-1  # k = 전단계 적은 마지막 수 인덱스
  while k <= n and dp[k] != INF:
    remain = m

    for j in range(k+1, n+1):
      remain -= num[j-1]
      if remain >= 0:
        dp[i][j] = min(dp[i][j], dp[i-1][k]+(remain**2))
      else:
        break
      remain -= 1
    k += 1
  if dp[i][n] != INF:
    print(min(dp[i-1]))
    break

# 전 줄의 남은 칸 제곱이 조금 늘어나더라도 현재 줄의 남은 칸 제곱을 많이 줄일 가능성이 있다.
# 배열에 i번째 줄에 j번째 사람까지 입력했을때에 남는칸 제곱의 최소값을 저장한다.
# 마지막 사람까지 적을 수 있는 줄을 찾았을 때 더이상 계산하는 것이 의미 없으므로 계산을 마무리하여 시간초과를 피한다.