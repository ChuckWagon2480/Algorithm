MAX = 10**9
n = int(input())

dp = [[dict() for _ in range(10)]for _ in range(n+1)]  # dp[자리수][숫자]
for j in range(1, 10):
  dp[1][j][1 << j] = 1

for i in range(2, n+1):
  for key, value in dp[i-1][1].items():
    try:
      dp[i][0][key | 1 << 0] += value
    except:
      dp[i][0][key | 1 << 0] = value

  for j in range(1, 9):
    for key, value in dp[i-1][j-1].items():
      try:
        dp[i][j][key | 1 << j] += value
      except:
        dp[i][j][key | 1 << j] = value
    for key, value in dp[i-1][j+1].items():
      try:
        dp[i][j][key | 1 << j] += value
      except:
        dp[i][j][key | 1 << j] = value

  for key, value in dp[i-1][8].items():
    try:
      dp[i][9][key | 1 << 9] += value
    except:
      dp[i][9][key | 1 << 9] = value

ans = 0
for i in range(10):
  try:
    ans += (dp[n][i][int('0b1111111111', base=2)])
  except:
    pass
print(ans % MAX)

# 처음엔 문제를 잘못 이해해 0~9를 포함하는 조건을 생각하지 않고 계단 수 구함 (쉬운계단수 문제와 동일하게)
# 거쳐온 경로를 남기기 위해 비트마스킹과 딕셔너리 활용
# 마지막에 나머지 연산 이상하게 해서 두번의 오답
