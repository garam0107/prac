def even_elements(A):
    item = A.pop(0)
    new_elements = []
    new_elements.extend(list(item))

    return new_elements


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
