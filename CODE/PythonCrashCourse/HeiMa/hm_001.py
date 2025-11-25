# 循环5次
# range(n)：生成[0,n)之间的整数
for i in range(5):
    if i == 3:
        print("不打印3")
        continue
    print(i)
