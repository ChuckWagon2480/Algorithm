import sys
input = sys.stdin.readline

MAX = 987654321

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
for _ in range(m):
  a, b, c = map(int, input().split())
  bus[a].append((b, c))

start, end = map(int, input().split())

distance = [MAX]*(n+1)
visit = [False]*(n+1)


def sol(start):
  distance[start] = 0
  now = start
  while True:
    if sum(visit) == n:
      return
    for b in bus[now]:
      distance[b[0]] = min(distance[b[0]], distance[now]+b[1])
    visit[now] = True

    temp = MAX
    for i in range(1, n+1):
      if not visit[i] and temp >= distance[i]:
        temp = distance[i]
        now = i


sol(start)
print(distance[end])

# 다익스트라 알고리즘
# 정해진 a에서 b까지의 최단거리 알고리즘
# 특징: 음수간선 있는 경우 정답 x -> 벨만포드 활용
# 매번 최단거리 노드를 찾는 대신 힙큐를 활용해 개선가능
