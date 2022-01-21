import sys
input = sys.stdin.readline

n = int(input())
node = [list(map(int, input().split())) for _ in range(n)]
nodex = sorted(enumerate(node), key=lambda x: x[1][0])
nodey = sorted(enumerate(node), key=lambda x: x[1][1])
nodez = sorted(enumerate(node), key=lambda x: x[1][2])
edge = []
for i in range(n-1):
  x = abs(nodex[i][1][0]-nodex[i+1][1][0])
  y = abs(nodey[i][1][1]-nodey[i+1][1][1])
  z = abs(nodez[i][1][2]-nodez[i+1][1][2])

  edge.append((x, nodex[i][0], nodex[i+1][0]))
  edge.append((y, nodey[i][0], nodey[i+1][0]))
  edge.append((z, nodez[i][0], nodez[i+1][0]))

parent = list(range(n))
edge.sort(key=lambda x: x[0])


def find(u):
  if u != parent[u]:
    parent[u] = find(parent[u])
  return parent[u]


def union(u, v):
  parent[find(u)] = find(v)


ans = 0

for e in edge:
  d, u, v = e
  if find(u) != find(v):
    union(u, v)
    ans += d

print(ans)
