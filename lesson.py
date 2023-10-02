def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Not enough params"
    return inner


@input_error
def my_func(*args):
    name = args[0]
    phone = args[1]
    return f"Add {name = } {phone = }"


while True:
    user_input = input(">>>")
    if user_input == "exit":
        break
    print(my_func(*user_input.split()))
