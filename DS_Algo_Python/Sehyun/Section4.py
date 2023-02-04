def power(base, exponent):
  if exponent == 0:
    return 1
  else:
    return base * power(base, exponent-1)

# print(power(2,0)) # 1
# print(power(2,2)) # 4
# print(power(2,4)) # 16

def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num - 1)
  
# print(factorial(1)) # 1
# print(factorial(2)) # 2
# print(factorial(4)) # 24
# print(factorial(7)) # 5040

def productOfArray(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    return arr[0] * productOfArray(arr[1:])


# print(productOfArray([1,2,3])) #6
# print(productOfArray([1,2,3,10])) #60

def recursiveRange(num):
  if num == 1:
    return 1
  else:
    return num + recursiveRange(num-1)

# print(recursiveRange(6)) # 21 1+2+3+4+5+6
# print(recursiveRange(10)) # 55 

def fib(n):
  if n in [0, 1]:
    return n
  else:
    return fib(n-1) + fib(n-2)


# print(fib(4)) # 3
# print(fib(10)) # 55
# print(fib(28)) # 317811
# print(fib(35)) # 9227465

def reverse(s):
  if len(s) == 1:
    return s
  else:
    return s[-1] + reverse(s[:-1])

# print(reverse('python')) # 'nohtyp'
# print(reverse('appmillers')) # 'srellimppa'

def isPalindrome(s):
  if len(s) == 0:
    return True
  else:
    if s[0] != s[-1]:
      return False
    else:
      return isPalindrome(s[1:-1])

# print(isPalindrome('awesome')) # false
# print(isPalindrome('foobar')) # false
# print(isPalindrome('tacocat')) # true
# print(isPalindrome('amanaplanacanalpanama')) # true
# print(isPalindrome('amanaplanacanalpandemonium')) # false

def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
  if len(arr) == 0:
    return False
  if not(cb(arr[0])):
    return someRecursive(arr[1:], cb)
  return True


# print(someRecursive([1,2,3,4], isOdd)) # true
# print(someRecursive([4,6,8,9], isOdd)) # true
# print(someRecursive([4,6,8], isOdd)) # false

def flatten(arr):
  if type(arr[0]) != int:
    return flatten(arr[0])
  if len(arr) == 1:
    return arr
  else:
    return [arr[0]] + flatten(arr[1:])
    

# print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
# print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
# print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]
