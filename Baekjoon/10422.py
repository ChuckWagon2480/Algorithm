import sys
input = sys.stdin.readline

dp = [0]*(5001)
dp[0] = 1
dp[2] = 1
for i in range(4, 5001, 2):
  for j in range(i, 1, -2):
    dp[i] = (dp[i] + dp[j-2]*dp[i-j]) % 1000000007
t = int(input())

for _ in range(t):
  l = int(input())
  print(dp[l])
