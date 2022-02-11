from collections import deque
MAX = 2000

s = int(input())

visit = [[False]*MAX for _ in range(MAX)]


def sol():
  q = deque()
  q.append((1, 0))  # (이모티콘, 클립보드)
  visit[1][0] = True

  count = 0
  while q:
    for _ in range(len(q)):
      now, clip = q.popleft()
      if now == s:
        print(count)
        return

      if not visit[now][now]:
        q.append((now, now))
        visit[now][now] = True
      if clip != 0 and now+clip < MAX and not visit[now+clip][clip]:
        q.append((now+clip, clip))
        visit[now+clip][clip] = True
      if now - 1 > 0 and not visit[now-1][clip]:
        q.append((now-1, clip))
        visit[now-1][clip] = True
    count += 1


sol()
