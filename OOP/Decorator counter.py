def decorator(func):
    counted = 0

    def wrapper():
        nonlocal counted
        counted += 1
        print(f"Counter: {counted}")
        func()

    return wrapper


@decorator
def function():
    print('Hello, world!')


function()
function()
function()
