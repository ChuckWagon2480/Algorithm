prob = input()
stack = []

for now in prob:
  value = 0
  if now == '(' or now == '[':
    stack.append(now)
  elif now == ')':
    while True:
      if len(stack) == 0:
        print(0)
        exit()
      top = stack.pop()
      if top == '(':
        if value == 0:
          stack.append(2)
        else:
          stack.append(value*2)
        break
      elif top == '[':
        print(0)
        exit()
      else:
        value += top
  elif now == ']':
    while True:
      if len(stack) == 0:
        print(0)
        exit()
      top = stack.pop()
      if top == '[':
        if value == 0:
          stack.append(3)
        else:
          stack.append(value*3)
        break
      elif top == '(':
        print(0)
        exit()
      else:
        value += top

ans = 0
for s in stack:
  if s != '(' and s != '[':
    ans += s
  else:
    ans = 0
    break
print(ans)

# 괄호문제 - 스택활용의 전형적인 유형
# 1차시도 틀린 케이스 (런타임 에러 (IndexError)) - ']'
# 2차시도 틀린 케이스 (런타임 에러 (IndexError)) - '(())]'