# cook your dish here
t = int(input())
while t > 0:
  x, y = map(int, input().split())
  d = y // x
  if d * x < y:
    print(d)
  else:
    print(d - 1)
  t -= 1
