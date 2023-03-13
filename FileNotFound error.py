def foo():
    try:
        file_name = 'file.txt'
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f'No such file or directory'


print(foo())
