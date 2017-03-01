import os

instructions = [l.split()[0].split('x') for l in open('./input/{0}'.format(os.path.basename(__file__)))]
sqft = 0
ribbon = 0


def calc_ft(set):
    l, w, h = sorted([int(item) for item in set])
    return 3 * l * w + 2 * w * h + 2 * h * l


def calc_ribbon(set):
    l, w, h = sorted([int(item) for item in set])
    return 2 * l + 2 * w + l * w * h


for instruction in instructions:
    sqft += calc_ft(instruction)
    ribbon += calc_ribbon(instruction)
print(sqft,',',ribbon)
