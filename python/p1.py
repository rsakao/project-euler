# 10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
# 同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ.
# int a =10;

def solve(n: int):
  sum = 0
  for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0:
      sum += i
  return sum

def solve2(n: int):
  return sum([i for i in range(1, n) if i % 3 == 0 or i % 5 == 0])
