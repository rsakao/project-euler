# 13195 の素因数は 5, 7, 13, 29 である.
# 600851475143 の素因数のうち最大のものを求めよ.

def solve(n: int):
  if n <= 3:
    return n

  factors = []
  i = 2
  while n >= 3:
    while n % i == 0:
      factors.append(i)
      n = n / i
    i = i + 1
        
  return max(factors)

def solve_efficient(n: int):
  if n <= 3:
    return n

  factors = []
  while n % 2 == 0:
    factors.append(2)
    n = n // 2

  i = 3
  while i * i <= n:
    while n % i == 0:
      factors.append(i)
      n = n // i
    i += 2

  if n > 2:
    factors.append(n)

  return max(factors)
