import os

instructions = [l.split()[0].split('x') for l in open('./input/{0}'.format(os.path.basename(__file__)))][0][0]
santaset = instructions[::2]
roboset = instructions[1::2]
position = [0, 0]
santa = [0, 0]
robo = [0, 0]
presents = [[0, 0]]
presents2 = [[0, 0]]
for i in instructions:
    if i == '<':
        position[0] -= 1
    elif i == '^':
        position[1] -= 1
    elif i == '>':
        position[0] += 1
    elif i == 'v':
        position[1] += 1
    if not position in presents:
        presents.append([position[0], position[1]])
for i in santaset:
    if i == '<':
        santa[0] -= 1
    elif i == '^':
        santa[1] -= 1
    elif i == '>':
        santa[0] += 1
    elif i == 'v':
        santa[1] += 1
    if not santa in presents2:
        presents2.append([santa[0], santa[1]])
for i in roboset:
    if i == '<':
        robo[0] -= 1
    elif i == '^':
        robo[1] -= 1
    elif i == '>':
        robo[0] += 1
    elif i == 'v':
        robo[1] += 1
    if not robo in presents2:
        presents2.append([robo[0], robo[1]])
print(len(presents))
print(len(presents2))
