import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
maxResult, minResult = -9876543210, 9876543210


def cal(now, op, index):
  global maxResult, minResult
  if index == n:
    maxResult = max(now, maxResult)
    minResult = min(now, minResult)
    return

  for i in range(4):
    if op[i] != 0:
      op[i] -= 1
      if i == 0:
        cal(now+num[index], op, index+1)
      elif i == 1:
        cal(now-num[index], op, index+1)
      elif i == 2:
        cal(now*num[index], op, index+1)
      elif i == 3:
        cal(now//num[index] if now >= 0 else (-now//num[index])*(-1), op, index+1)
      op[i] += 1


cal(num[0], op, 1)

print(maxResult)
print(minResult)
