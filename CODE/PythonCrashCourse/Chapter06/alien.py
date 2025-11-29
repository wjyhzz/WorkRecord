alien_0 = {'color': 'green', 'points': 5}

# 添加x，y轴
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# 添加速度
alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

del alien_0['speed']
print(alien_0)
