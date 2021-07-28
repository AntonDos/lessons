import random


def search_sum_and_max(*args):
    args_sum = 0
    if len(args) == 0:
        return
    max_el = args[0]
    for element in args:
        if max_el is not None and element > max_el:
            max_el = element
        args_sum += element
    return args_sum, max_el


random_elements = []
for _ in range(10):
    random_el = random.randint(1, 100)
    random_elements.append(random_el)

args_sum, max_el = search_sum_and_max(*random_elements)
print(args_sum, max_el)
