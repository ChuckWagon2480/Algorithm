import bisect
import sys
input = sys.stdin.readline

MAX = 500001

n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort()

dp = [0]+[MAX]*n
log = [0]*MAX
ans = 0
for i in range(n):
  candi = bisect.bisect_left(dp, line[i][1])
  ans = max(ans, candi)
  log[line[i][1]] = dp[candi-1]
  if dp[candi] > line[i][1]:
    dp[candi] = line[i][1]

lis = set()
now = dp[ans]
while now != 0:
  lis.add(now)
  now = log[now]

print(n-ans)
for l in line:
  if l[1] not in lis:
    print(l[0])

# 겹치는 선이 많은 순서대로 제거하는 그리디(?) 방식으로 생각
# 10만개의 선들이 겹쳐지는 파악하는 대만 시간초과 예상됨
# 다른 대안 고려

# 전기줄 출발점 기준 정렬 -> 도착점 lis가 교차 없는 최대의 전기줄 수 (ans)
# 정답: n - ans
# 삭제할 전기줄을 알기 위해 log 기록