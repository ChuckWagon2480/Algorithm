import sys
input = sys.stdin.readline

n = int(input())
*num, target = map(int, input().split())

dp = [[0]*(21) for _ in range(n-1)]
# 행 i번째 숫자
# 열 i번째 숫자까지의 합

dp[0][num[0]] = 1

for i in range(1, n-1):
  for j in range(21):
    if dp[i-1][j] != 0:
      if j+num[i] < 21:
        dp[i][j+num[i]] += dp[i-1][j]
      if j-num[i] >= 0:
        dp[i][j-num[i]] += dp[i-1][j]

print(dp[n-2][target])

# DP
# i-1번째 숫자까지의 연산결과에 i번째 숫자를 더하거나 뺄 수 있을때
# 그 경우의 수를 더해준다