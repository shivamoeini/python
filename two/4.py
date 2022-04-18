n = int(input('tedad afrad ra vared konid:'))
dic_name = {}
for i in range(1, n + 1):
    name = input(f'nam fard {i} ra vared konid:')
    sen = input(f'sen fard {i} ra vared konid:')
    dic_name[name] = sen
print(dic_name)
