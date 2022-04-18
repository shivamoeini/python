n=int(input('tedad dros ra vared konid'))
num_kol=0
num_vahed_kol=0
for i in range(n) :
    vahed=int(input(f" vahed dars {i} ra vared konid"))
    nomre=float(input(f" nomre dars {i} ra vared konid"))
    num_kol+=nomre*vahed
    num_vahed_kol+=vahed
average=num_kol/num_vahed_kol
print(f"moadel kol shoma barabar ast ba {average}")
