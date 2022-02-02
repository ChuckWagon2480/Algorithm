from collections import deque
MAX = 100001

n, k = map(int, input().split())


def bfs(n, k):
  visit = [0]*MAX
  distance = [-1]*MAX

  q = deque()
  q.append(n)
  visit[n] = 1
  distance[n] = 0

  while q:
    now = q.popleft()

    if now == k:
      print(distance[now])
      return

    if now*2 < MAX and visit[now*2] == 0:
      q.appendleft(now*2)
      visit[now*2] = 1
      distance[now*2] = distance[now]
    for next in [now+1, now-1]:
      if 0 <= next < MAX and visit[next] == 0:
        q.append(next)
        visit[next] = 1
        distance[next] = distance[now]+1


bfs(n, k)

# 일반적인 bfs와 달리 순간이동이 0초 걸리므로 큐의 앞에 넣는방식으로 해결한다