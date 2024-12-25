import time

def fib(n):
    if n == 1 or n == 2:
        return 1


    a, b = 1, 1


    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


def measure_time():
    test_values = [5, 10, 15, 20, 30]

    for n in test_values:
        start_time = time.time()
        result = fib(n)
        end_time = time.time()

        elapsed_time = (end_time - start_time) * 1000
        print(f"fib({n}) = {result}, время выполнения: {elapsed_time:.3f} миллисекунд")

measure_time()
