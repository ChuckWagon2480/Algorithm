import sys
input = sys.stdin.readline


def find(n):
  if n != parent[n]:
    parent[n] = find(parent[n])
  return parent[n]


def union(a, b, c):
  global edgeCount, ans
  if find(a) == find(b):
    return
  else:
    parent[find(a)] = find(b)
    edgeCount += 1
    ans += c


v, e = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(e)]

parent = list(range(v+1))
ans = 0

edgeCount = 0
edge.sort(key=lambda x: x[2], reverse=True)

for _ in range(e):
  if edgeCount == v-1:
    break
  a, b, c = edge.pop()
  union(a, b, c)

print(ans)

# kruskal 알고리즘 find / union 활용