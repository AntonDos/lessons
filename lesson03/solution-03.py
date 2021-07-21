my_list = [1, 2, 'w', 3]
my_new_list = []
for x in my_list:
    new_element = str(x)
    my_new_list.append(new_element)
my_new_list
my_new_list[::-1]
''.join(my_new_list[::-1])
"".join([str(x)] for x in my_list[::-1])
"".join(map(my_list[::-1], str))
