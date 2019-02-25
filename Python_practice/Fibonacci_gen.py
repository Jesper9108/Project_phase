def fibonacci(n):
    a, b = 0, 1
    for fib_num in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(100):
    print(number)