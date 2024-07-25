# # clear
# person = {'name': 'Alice', 'age': 25}

# # get
# person = {'name': 'Alice', 'age': 25}
# print(person.get('name'))

# # keys
# person = {'name': 'Alice', 'age': 25}
# # print(person.keys())
# # for k in person.keys():
# #     print(k)
# # values
# person = {'name': 'Alice', 'age': 25}
# # for v in person.values():
# #     print(v)
# # items
# person = {'name': 'Alice', 'age': 25}
# # for key,value in person.items():
# #     print(key,value)
# # pop
# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age'))
# print(person)
# print(person.pop('country', None))
# # setdefault
person = {'name': 'Alice', 'age': 25}
person.setdefault('name')
print(person)
# update 
# person = {'name': 'Alice', 'age': 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}

# person.update(other_person)
# print(person) # {'name': 'Jane', 'age': 25, 'gender': 'Female'}

# person.update(age = 50, country = 'KOREA')
# print(person) # {'name': 'Jane', 'age': 50, 'gender': 'Female', 'country': 'KOREA'}


# a = {}

# b = {'name': 'Alice', 'age': 25}

# a.update(b)

# print(a)


# b.update(country = 'KOREA')

# print(a)
# print(b)