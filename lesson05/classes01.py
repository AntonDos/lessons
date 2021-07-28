def format_string(name):
    return f"Hello, {name}"


my_names = {"Alex", "Olga", "Roma", "Dima", "Kiril"}
for my_name in my_names:
    my_string = format_string(my_name)
    print(my_string)
