# How to find the sum of the digits of a positive integer number using recursion?

def sumOfDigits(n):
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  if n == 0:
    return 0
  return n % 10 + sumOfDigits(n // 10)


def sumOfDigits2(n):
  return sum([int(x) for x in str(n)])


# print(sumOfDigits2(12345))


# How to calculate power of a number using recursion?
def powerOfNumber(x, n):
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  if n == 0:
    return 1
  return x * powerOfNumber(x, n - 1)


# How to find GCD (Greatest Common Divisor) of two numbers using recursion?
# Euclidean Algorithm
def gcd(a, b):
  assert int(a) == a and int(b) == b, "The number must be positive integer only!"
  if b == 0:
    return a
  return gcd(b, a % b)

# print(gcd(48, 18))
# print(gcd(18, 48))

# How to convert a number from Decimal to Binary using recursion
def decimalToBinary(n):
  assert int(n) == n, "The number must be positive integer only!"
  if n == 0:
    return 0
  return n % 2 + 10 * decimalToBinary(n // 2)

def decimalToBinary2(n):
  return int(bin(n).replace("0b", ""))

def decimalToBinary3(n):
  return int(bin(n)[2:])

def decimalToBinary4(n):
  return format(n, 'b')

def decimalToBinary5(n):
  return "{0:b}".format(n)

def decimalToBinary6(n):
  return bin(n)[2:]

def decimalToBinary7(n):
  if n == 1:
    return "1"
  else:
    return decimalToBinary7(n // 2) + str(n % 2)
  
  
print(decimalToBinary7(8))