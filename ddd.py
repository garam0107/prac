# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    pass
    new_dict = {}
    for _ in blood_types:
       new_dict['A'] = blood_types.count('A')
       new_dict['B'] = blood_types.count('B')
       new_dict['O'] = blood_types.count('O')
       new_dict['AB'] = blood_types.count('AB')
       return new_dict


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    pass
    new = {}
    for A in blood_types:
        new[A] = 
    
    

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
