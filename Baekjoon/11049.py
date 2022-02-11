import sys
input = sys.stdin.readline

n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[-1]*(n) for _ in range(n)]


def sol(x, y):
  if dp[x][y] != -1:
    return dp[x][y]
  if x == y:
    return 0
  if y == x+1:
    return matrix[x][0]*matrix[x][1]*matrix[y][1]

  for i in range(x, y):
    left = sol(x, i)
    right = sol(i+1, y)
    if dp[x][y] == -1 or dp[x][y] > left+right + matrix[x][0]*matrix[i][1]*matrix[y][1]:
      dp[x][y] = left+right + matrix[x][0]*matrix[i][1]*matrix[y][1]

  return dp[x][y]


print(sol(0, n-1))
