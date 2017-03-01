import os,hashlib

instructions = [l.split()[0].split('x') for l in open('./input/{0}'.format(os.path.basename(__file__)))][0][0]

for x in range(8223372036854775807):
    temp = instructions + str(x)
    if hashlib.md5(temp.encode('utf-8')).hexdigest()[:6] == '000000':
        print(x)
        break