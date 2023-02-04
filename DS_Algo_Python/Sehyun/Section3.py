# How to find the sum of the digits of a positive integer number using recursion?

def sumOfDigits(n):
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  if n == 0:
    return 0
  return n % 10 + sumOfDigits(n // 10)


def sumOfDigits2(n):
  return sum([int(x) for x in str(n)])


print(sumOfDigits2(12345))