def debug(print_input=False, print_output=False):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if print_input:
                input_str = "Input:"
                if args:
                    input_str += f" {args}"
                if kwargs:
                    input_str += f", {kwargs}"
                print(input_str)

            output_result = func(*args, **kwargs)

            if print_output:
                print(f"Output: {output_result}")

            return output_result

        return wrapper

    return decorator


@debug(print_input=True, print_output=False)
def add(x, y):
    return x + y


result = add(2, 3)
