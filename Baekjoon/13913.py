from collections import deque


MAX = 100001
n, k = map(int, input().split())

visit = [False] * MAX
history = [-1] * MAX
count = 0


def bfs(n, k):
  global count
  q = deque()
  q.append(n)
  visit[n] = True

  while q:
    for _ in range(len(q)):
      now = q.popleft()
      if now == k:
        return

      for next in [now-1, now+1, now*2]:
        if 0 <= next < MAX and not visit[next]:
          q.append(next)
          visit[next] = True
          history[next] = now

    count += 1


bfs(n, k)
how = []
while k != -1:
  how.append(k)
  k = history[k]
how.reverse()

print(count)
print(*how)

# history 배열을 활용해 방문할때 이전위치를 기록해둔다