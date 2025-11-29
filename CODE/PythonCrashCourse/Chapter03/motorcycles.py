motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'

motorcycles.append('哈雷')

motorcycles.insert(0, "雅迪")
# ['雅迪', 'ducati', 'yamaha', 'suzuki', '哈雷']
motorcycles.remove('雅迪')
print(motorcycles)

# del motorcycles[0]
# print(motorcycles.pop())
# print(motorcycles.pop(0))

# print(motorcycles.index('dianji'))
# print(motorcycles.count('dianji'))

motorcycles.clear()
print(motorcycles)
