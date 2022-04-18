my_list = []
qeymat_kol = 0
for i in range(1, 11):
    y = input(f"vard kon noe takhalof {i}:")
    x = int(input(f"vard kon qeymat takhalof {y}:"))
    my_list.append([x, y])
    qeymat_kol += x
print(f'jame kolo qeymat takhalofat shomahast:{qeymat_kol}')
