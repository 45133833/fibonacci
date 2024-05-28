Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fibonacci_generator():
  x = int(input("Tell me Number sequance: "))
  a = 0
  b = 1
  for i in range(x):
    print(b)
    a, b = b, a + b

fib = fibonacci_generator()