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

# N의 범위가 최대 11이므로 연산자 개수가 제한없다고 러프하게 계산했을때 4**10 -> 2**20이므로 제한시간 안에 모든 경우의수를 확인할 수 있다.