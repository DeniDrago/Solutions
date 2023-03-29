from datetime import datetime


def login_required(func):

    def wrapper(*args, **kwargs):
        login = input('Enter your login: ')
        password = input('Enter your password: ')
        if (login, password) in users:
            return func(*args, **kwargs)
        else:
            print('Incorrect login or password')

    return wrapper


users = [("user1", "password1"), ("user2", "password2"), ("user3", "password3")]


@login_required
def my_function():
    with open("data.txt", "w") as f:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Accessed at: {current_time}")
    with open("data.txt", "r") as f:
        data = f.read()
    return data


print(my_function())
