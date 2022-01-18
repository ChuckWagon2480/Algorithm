from itertools import combinations
import sys
input = sys.stdin.readline

alpha = set('bdefghjklmopqrsuvwxyz')

n, k = map(int, input().split())
words = []
for _ in range(n):
  w = 0
  for i in set(input()[4:-4])-set('antatica'):
    w |= 1 << (ord(i)-ord('a'))
  words.append(w)

ans = 0

if k >= 5:
  for now in combinations(alpha, k-5):
    check = 0
    for i in now:
      check |= 1 << (ord(i)-ord('a'))
    temp = 0
    for w in words:
      if w & check == w:
        temp += 1
    ans = max(ans, temp)

print(ans)

# 첫 시도 - 시간초과
# set 차집합 연산의 동작방식과 시간복잡도를 제대로 알지 못함
# 비트마스킹을 활용해 케이스별로 단어를 읽을 수 있는지 빠르게 비교하도록 개선하여 해결

