def fib(n):
    fib_array = [0, 1]
    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])

    print(fib_array)

fib(8)
