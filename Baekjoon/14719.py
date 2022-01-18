h, w = map(int, input().split())
block = list(map(int, input().split()))
ans = 0
for i in range(1, max(block)+1):
  start = False
  temp = 0
  for j in range(w):
    if block[j] >= i:  # 블록
      ans += temp
      start = True
      temp = 0
    elif start:
      temp += 1

print(ans)
