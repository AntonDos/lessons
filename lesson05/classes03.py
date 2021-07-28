import random

def seach_min_and_max(*args, **kwargs):
    func_type = kwargs["func_type"]
    min_el = args[0]
    max_el = args[0]
    for element in args:
        if element < args:
            min_el = element
        if element > max_el:
            max_el = element




random_elements = []
for _ in range(10):
    random_el = random.randint(1, 100)
    random_elements.append(random_el)

min_el = search_min_and_max(*random_elements, func_type="")
print

