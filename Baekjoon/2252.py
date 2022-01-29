import sys
from collections import deque

n, m = map(int, input().split())
student = [set() for _ in range(n+1)]
count = [0]*(n+1)
ans = []

for _ in range(m):
  a, b = map(int, input().split())
  student[b].add(a)
  count[a] += 1

q = deque()
for i in range(1, n+1):
  if count[i] == 0:
    q.append(i)

while q:
  now = q.popleft()
  ans.append(now)
  for s in student[now]:
    count[s] -= 1
    if count[s] == 0:
      q.append(s)

ans.reverse()
print(*ans)

# 위상정렬
# 뒤에 누군가 없어도 되는 학생부터 역순으로 줄세우는 접근
# 성공은 했으나 뒤에서 부터 줄세우고 역순으로 뒤집느라 시간이 오래 걸렸다...
# 보통은 내가 생각한것과 반대로 앞에 누군가 없어도 되는 학생부터 앞에서부터 세우는 식으로 접근.