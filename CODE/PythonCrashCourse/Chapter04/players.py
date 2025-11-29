players = ['a', 'b', 'c', 'd', 'e']
# ['a', 'b', 'c']
print(players[0:3])
# ['a', 'b', 'c', 'd']
print(players[:4])
# ['c', 'd', 'e']
print(players[2:])
# ['c', 'd', 'e']
print(players[-3:])
# ['a', 'b', 'c', 'd', 'e']
print(players[:])

for player in players[:3]:
    print(player)
