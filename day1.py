import os
instructions = [l.split() for l in open('./input/{0}'.format(os.path.basename(__file__)))][0][0]
floor = 0
step = 0
for i in instructions:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
    step += 1
    if floor == -1:
        print(step)
print(floor)