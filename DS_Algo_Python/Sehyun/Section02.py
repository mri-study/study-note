def factorial(n):
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  if n == 1:
    return 1
  return n * factorial(n-1)

print(factorial(-3))

def fibo(n):
  assert n >= 0 and int(n) == n, "The number must be positive integer only!"
  if n in [0, 1]:
    return n
  else:
    return fibo(n-1)  + fibo(n-2)

fibo(5)