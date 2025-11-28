# 定义一个大小不可变的矩形
dimensions = (200, 50)
#报错
# dimensions[0] = 150

# 定义只包含一个元素的元组
my_t = (3,)
print(my_t[0])

#元组遍历
for dimension in dimensions:
   print(dimension)