def recursive_factorial(x):
    if x > 0:
        return x * recursive_factorial(x-1)
    else:
        return 1


print(recursive_factorial(5))
