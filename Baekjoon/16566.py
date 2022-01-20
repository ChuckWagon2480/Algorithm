import bisect
from functools import cached_property
import sys
input = sys.stdin.readline


def find(u):
  if u != parent[u]:
    parent[u] = find(parent[u])
  return parent[u]


def union(u):
  parent[u] = find(u+1)


n, m, k = map(int, input().split())
cards = list(map(int, input().split()))
target = list(map(int, input().split()))
parent = list(range(m+1))

cards.sort()
for t in target:
  candi = bisect.bisect_right(cards, t)
  ans = find(candi)
  print(cards[ans])
  union(ans)

# 첫 시도 코드
# heapq.heapify(cards)
# target = list(enumerate(target))
# print(target)
# target.sort(key=lambda x: x[1])
# print(target)
# ans = [0]*k
# for i, t in target:
#   now = heapq.heappop(cards)
#   while now <= t:
#     now = heapq.heappop(cards)
#   ans[i] = now

# for a in ans:
#   print(a)

# 첫 시도 반례 2 1 1 2 2
# 출력: 4 2 3 5 7
# 정답: 3 2 4 5 7
# 힙을 활용해 상대의 작은 숫자부터 해결하려 했지만 위의 코드는 그때마다 최대한 작은 수 를 내야하는 조건에서 반례가 생김

# 이진탐색으로 upper bound를 찾아 하나씩 정답을 출력
# 사용한 카드가 다시 사용되지 않고 빠르게 다음 카드를 알기위해 disjoint set을 활용
