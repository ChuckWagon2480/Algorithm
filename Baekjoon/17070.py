import sys
input = sys.stdin.readline


def check(move, pos):
  x, y = pos
  if move == 0:
    nx, ny = x, y+1
    if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0:
      return True
    else:
      return False
  elif move == 1:
    nx, ny = x+1, y
    if (0 <= nx < n) and (0 <= ny < n) and graph[nx][ny] == 0:
      return True
    else:
      return False
  elif move == 2:
    for m in [(1, 0), (0, 1), (1, 1)]:
      nx, ny = x+m[0], y+m[1]
      if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] != 0:
        return False
    return True


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
  for j in range(1,n):
    for k in range(3):
      if dp[i][j][k] > 0:
        # 가로이동
        if k != 1 and check(0, (i, j)):
          dp[i][j+1][0] += dp[i][j][k]
        # 세로이동
        if k != 0 and check(1, (i, j)):
          dp[i+1][j][1] += dp[i][j][k]
        # 대각선이동
        if check(2, (i, j)):
          dp[i+1][j+1][2] += dp[i][j][k]

print(sum(dp[n-1][n-1]))

# 단순하게 bfs 진행했을때 시간초과
# top left에서 bottom right방향으로 이동하므로 차례로 dp진행해주면서
# 모든 경우의 수가 아닌 같은 위치에 같은 상태인것 끼리 모아서 한번에 이동시켜주는 느낌
