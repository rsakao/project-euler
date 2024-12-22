# フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 数列の項の値が400万以下のとき, 値が偶数の項の総和を求めよ.

def solve(n: int):
  fib = fibonacci(n)
  return even_numbers_sum(fib)

def fibonacci(n: int):
  array = [1, 2]
  while True:
    new_element = array[-1] + array[-2]
    if new_element > n:
      break
    array.append(new_element)
  return array

def even_numbers_sum(a):
  return sum([i for i in a if i % 2 == 0])

def optimized_fibonacci_sum(n: int):
  a, b = 1, 2
  total = 0
  while a <= n:
    if a % 2 == 0:
      total += a
    a, b = b, a + b
  return total
