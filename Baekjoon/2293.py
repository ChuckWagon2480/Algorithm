import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [1] + [0]*k

for c in coin:
  for i in range(c, k+1):
    dp[i] += dp[i-c]

print(dp[k])

# 동전이 배수라는 조건x -> DP