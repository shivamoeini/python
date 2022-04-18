list_takhalofat = []
qeymat_kol = 0
name = input('enter driver name:')
car_color = input('enter car color')
car_number = input('enter car number')
for i in range(1, 11):
    y = input(f"vard kon noe takhalof {i}:")
    x = int(input(f"vard kon qeymat takhalof {y}:"))
    list_takhalofat.append([x, y])
    qeymat_kol += x
print(f'esm ranande: {name} rang mashine:{car_color} shomare mashine:{car_number}')
print('list takhalofat')
for i in list_takhalofat:
    print(i)
print(f'jame kolo qeymat takhalofat shomahast:{qeymat_kol}')
