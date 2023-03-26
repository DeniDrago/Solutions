def retry(max_retries, exc):

    def decorator(func):

        def wrapper(*args, **kwargs):
            retries = 0
            while retries <= max_retries:
                try:
                    return func(*args, **kwargs)
                except exc as e:
                    retries += 1
                    if retries > max_retries:
                        return e

        return wrapper

    return decorator


@retry(max_retries=3, exc=(ZeroDivisionError, TypeError))
def function(a, b):
    return a / b


print(function(6, 2))
print(function(9, 2))
print(function(10, 0))
print(function(40, 'f'))
