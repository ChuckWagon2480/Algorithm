from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

visit = [[-1]*m for _ in range(n)]


def sol(x1, y1, x2, y2):
  q = deque()
  q.append((x1, y1))
  visit[x1][y1] = 0

  while q:
    x, y = q.popleft()
    if x == x2 and y == y2:
      print(visit[x][y])
      return
    for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      for i in range(1, k+1):
        nx, ny = x+move[0]*i, y+move[1]*i
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
          if visit[nx][ny] == -1:
            q.append((nx, ny))
            visit[nx][ny] = visit[x][y]+1
          elif visit[nx][ny] <= visit[x][y]:
            break
          else:
            continue
        else:
          break

  print(-1)


sol(x1-1, y1-1, x2-1, y2-1)

# bfs문제이지만 더이상 진행해야하는 경우와 불필요한 진행을 줄여야 시간내에 해결할 수 있었다.
# 같은 턴에 방문한 곳은 쭉 더 가봐야하고 이전에 이미 방문한 경우에는 큐에 이미 들어가서 4가지 방향으로 더 진행했을 것이기 때문에
# 그 이상 방문여부를 확인할 필요가 없다