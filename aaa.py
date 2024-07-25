my_list = [1,2,3,4,5,6,7,8,9,10]
A = []

for i in my_list:
    if i % 2 == 1:
        
        my_list.pop(i)
        
    print(my_list)



A =[]
my_list = [1,2,3,4,5,6,7,8,9,10]

items = my_list.pop(1)

A.extend([items])

print(A)
            


