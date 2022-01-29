n = int(input())


def sol(n):
  num = list(range(10))
  if n < 10:
    print(num[n])
    return

  i = 1
  while i < len(num):
    for j in range(10):
      if num[i] % 10 <= j:
        break
      num.append(num[i]*10+j)
    if i == n:
      print(num[n])
      return
    i += 1
  print(-1)


sol(n)

# 감소하는 수 중 최대값: 9876543210
# 작은 수부터 차례로 감소하는수를 만들어가며 모든 감소하는 수 확인