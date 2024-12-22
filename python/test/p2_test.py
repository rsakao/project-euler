import unittest
from python.p2 import solve, optimized_fibonacci_sum

class TestFibonacciSum(unittest.TestCase):
  def test_solve_3(self):
    self.assertEqual(solve(3), 2)

  def test_solve_10(self):
    self.assertEqual(solve(10), 10)  # 2 + 8 = 10

  def test_solve_34(self):
    self.assertEqual(solve(34), 44)  # 2 + 8 + 34 = 44

  def test_solve_4000000(self):
    self.assertEqual(solve(4000000), 4613732)

  def test_optimized_fibonacci_sum_3(self):
    self.assertEqual(optimized_fibonacci_sum(3), 2)

  def test_optimized_fibonacci_sum_10(self):
    self.assertEqual(optimized_fibonacci_sum(10), 10)  # 2 + 8 = 10

  def test_optimized_fibonacci_sum_34(self):
    self.assertEqual(optimized_fibonacci_sum(34), 44)  # 2 + 8 + 34 = 44

  def test_optimized_fibonacci_sum_4000000(self):
    self.assertEqual(optimized_fibonacci_sum(4000000), 4613732)

if __name__ == '__main__':
  unittest.main()
