import sys
input = sys.stdin.readline

n, k = map(int, input().split())
elec = list(map(int, input().split()))
ans = 0
plug = set()
i = 0
while len(plug) < n and i < k:
  plug.add(elec[i])
  i += 1

while i < k:
  if elec[i] in plug:
    i += 1
  else:
    candi = list(plug)[0]
    next = i
    for p in plug:
      try:
        check = elec.index(p, i)
        if check > next:
          candi = p
          next = check
      except:
        candi = p
        break
    plug.remove(candi)
    plug.add(elec[i])
    ans += 1
    i += 1

print(ans)

# 그리디 문제 - 앞으로 안쓰거나 가장 나중에 쓸것을 뺀다
# n, k가 크지 않아 탐색 시간도 충분