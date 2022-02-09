import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
count = int(input())
ans = 0
value = [sum(num[0:count])]
for i in range(count, n):
  value.append(value[i-count]-num[i-count]+num[i])

front = [value[0]]
rear = [value[-1]]

for i in range(1, len(value)-(count*2)):
  front.append(max(front[-1], value[i]))
  rear.append(max(rear[-1], value[-(1+i)]))

for f in range(len(front)):
  ans = max(ans, front[f]+value[f+count]+rear[-1-f])
print(ans)

# 소형기관차 3개를 앞 중간 뒤로 나눈다.
# front - 앞 기차가 태울 승객 최대치
# rear - 뒷 기차가 태울 승객 최대치
# 중간기차의 승객과 앞, 뒤 기차의 최대값의 합에 대해서 그 중 최대값을 찾는다.