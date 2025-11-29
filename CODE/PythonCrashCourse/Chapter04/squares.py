"""
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
"""
squares = []
squares = [value ** 2 for value in range(1, 11)]

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
