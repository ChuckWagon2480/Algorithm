from collections import deque


n, k = map(int, input().split())

visit = [-1]*(10**5 + 1)  # visit 방문여부
dp = [0]*(10**5 + 1)  # dp 경우의 수


def bfs():
  q = deque()
  visit[n] = 0
  dp[n] = 1
  q.append(n)

  cnt = 0
  while True:
    if visit[k] != -1:
      print(visit[k])
      print(dp[k])
      return
    cnt += 1

    for _ in range(len(q)):
      now = q.popleft()

      for next in [now-1, now+1, now*2]:
        if 0 <= next <= 100000:
          if visit[next] == -1:
            q.append(next)
            visit[next] = cnt
          if cnt == visit[next]:
            dp[next] += dp[now]


bfs()

# 단순히 bfs 수행했을때 시간초과
# 경우의 수를 세면서 같은 시점 같은 위치라면 동시에 진행될 수 있도록
