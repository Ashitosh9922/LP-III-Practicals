def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# Take user input
n = int(input("Enter the value of n: "))

# Recursive result
rec_result = fibonacci_recursive(n)
print(f"Recursive Fibonacci of {n}: {rec_result}")

# Iterative result
iter_result = fibonacci_iterative(n)
print(f"Iterative Fibonacci of {n}: {iter_result}")
