tedad_karmandan = int(input('tedad karmandan ra vared konid'))
list_karmandan = []
for number in range(1, tedad_karmandan+1):
     shomare_kart = int(input(f" shomare kart karmand shomare {number} ra vared konid"))
     saat_kar = int(input(f'saat kari karmand shomare {number} ra vared konid'))
     list_karmandan.append([saat_kar, shomare_kart])
for karmand in list_karmandan:
     hoghugh = 0
     if karmand[0] <= 160:
         hoghugh = karmand[0] * 100000
     elif karmand[0] <= 200:
         ezafe_kar = karmand[0] - 160
         hoghugh = (ezafe_kar * 50000) + (160 * 100000)
     elif karmand[0] > 200:
         hoghugh = (40 * 50000) + (160 * 100000)
     print(f"hoghugh karmand shoma ba shomare karmandi {karmand[1]} hast {hoghugh}")

