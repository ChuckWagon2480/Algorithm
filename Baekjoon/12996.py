import sys
input = sys.stdin.readline

s, a, b, c = map(int, input().split())
dp = [[[[-1]*(51) for _ in range(51)] for _ in range(51)] for _ in range(51)]


def sol(s, a, b, c):
  if s == 0:
    if a == 0 and b == 0 and c == 0:
      return 1
    else:
      return 0

  if dp[s][a][b][c] != -1:
    return dp[s][a][b][c]
  else:
    dp[s][a][b][c] = 0

  for na, nb, nc in [(a-1, b, c), (a, b-1, c), (a, b, c-1), (a-1, b-1, c), (a-1, b, c-1), (a, b-1, c-1), (a-1, b-1, c-1)]:
    if na < 0 or nb < 0 or nc < 0:
      continue
    dp[s][a][b][c] += sol(s-1, na, nb, nc)

  dp[s][a][b][c] %= 1000000007
  return dp[s][a][b][c]


print(sol(s, a, b, c))

# dp 4차원 배열을 활용
# dp[s][a][b][c] -> s곡을 각자 a개 b개 c개 남았을때 경우의 수
# 0곡 이고 각자 모든 곡을 다 부르고 0개 남은경우 경우 하나에서 시작