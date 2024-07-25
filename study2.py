# add
my_set = {'a', 'b', 'c', 1, 2, 3}

my_set.add(4)
print(my_set)

my_set.add(4)
print(my_set)
# clear
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.clear()
print(my_set)
# remove
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.remove('a')
print(my_set)
# pop
my_set = {'a', 'b', 'c', 1, 2, 3}
e = my_set.pop()
print(e)
print(my_set)
# discard
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.discard(2)
print(my_set)
my_set.discard(10)
# update
my_set = {'a', 'b', 'c', 1, 2, 3}
my_set.update([1,4,5]) 
print(my_set) # {1, 2, 3, 'c', 4, 5, 'a', 'b'} -> 해시 테이블의 순서대로 출력
                                                # 재실행시 해시 함수가 재실행되서 해시 테이블이 새로 지정되서 새로운 값 출력
# 집합 메서드
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.issubset(set2)) # False
print(set3.issubset(set1)) # True
print(set1.issuperset(set2)) #False
print(set1.issuperset(set3)) #True
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9} -> 재실행하여도 똑같은 순서로 출력
print(set1 - set2)
    
    