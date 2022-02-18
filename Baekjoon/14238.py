from collections import Counter
import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
sCounter = Counter(s)
ans = ['']*n

visit = [[[[[False]*3 for _ in range(3)] for _ in range(sCounter['C']+1)]
          for _ in range(sCounter['B']+1)]for _ in range(sCounter['A']+1)]


def dfs(a, b, c, prev, pprev):
  if a+b+c == n:
    return True

  if visit[a][b][c][prev][pprev]:
    return False

  visit[a][b][c][prev][pprev] = True

  if a+1 <= sCounter['A']:
    ans[a+b+c] = 'A'
    if dfs(a+1, b, c, 0, prev):
      return True
  if b+1 <= sCounter['B'] and prev != 1:
    ans[a+b+c] = 'B'
    if dfs(a, b+1, c, 1, prev):
      return True
  if c+1 <= sCounter['C'] and prev != 2 and pprev != 2:
    ans[a+b+c] = 'C'
    if dfs(a, b, c+1, 2, prev):
      return True
  return False


if dfs(0, 0, 0, -1, -1):
  print(''.join(ans))
else:
  print(-1)

# dfs를 전부 진행했을때 시간초과
# 이번 출근자를 결정할 때 전날과 전전날만 영향을 주며 그전에 어떻게 구성되어있더라도 a,b,c 사용횟수가 같다면 같은 경우로 본다.
# 위처럼 생각했을때 방문여부를 기록하고 dfs를 진행하며 빠르게 가지치기 할 수 있도록 한다.