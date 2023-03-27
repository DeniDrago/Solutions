def memorize(max_size=100):
    caches = {}

    def decorator(func):

        def wrapper(*args):
            if args in caches:
                return f'{caches[args]} (from the cache)'
            result = func(*args)
            if len(caches) == max_size:
                key_to_remove = list(caches.keys())[0]
                caches.pop(key_to_remove)
            caches[args] = result
            return result

        return wrapper

    return decorator


@memorize()
def foo(n):
    return n * 2


print(foo(5))
print(foo(5))
print(foo(6))
print(foo(3))
print(foo(3))
print(foo(3))
