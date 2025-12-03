# name = {}
# age = {}
# for i in range(3):
#     name[i] = input('输入姓名：')
#     age[i] = input('输入年龄：')
#
# for j in range(3):
#     print(name[j] + ' ' + age[j])
def func(list1):
    list1[0] = 10


my_list = [1, 2]
func(my_list)
print(my_list)
