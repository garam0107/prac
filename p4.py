
T = 3
for t in range(1, T + 1):
    arr = [22,8,5,123,7,2,63,7,3,46]
    A = 0
    for n in arr:
        A += n
        num =  A / len(arr)
print('#' + str(t), str(num))      


# # # import sys
# # # sys.stdin = open("input.txt", "r")
# T = 3
# # # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for t in range(1, T + 1):
#     arr = [1,3,4,5,6,7,8,6,144]
#     A = 0
#     for i in arr:
#         A += i
#         num = A / len(arr)


# T = int(input())
# for t in range(1, T + 1):
#     arr = list(map(int,input().split()))
#     A = 0
#     for n in arr:
#         A += n
#         num = int(A / len(arr))
# print('#'+str(t), str(num))