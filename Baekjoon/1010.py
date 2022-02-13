import sys
input = sys.stdin.readline

f = [1, 1]+[-1]*29

def fact(num):
  if f[num] != -1:
    return f[num]

  f[num] = num*fact(num-1)
  return f[num]


t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  result = fact(m)//(fact(n)*fact(m-n))
  print(result)