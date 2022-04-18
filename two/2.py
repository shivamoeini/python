n = 0
h = 0
sum_list = []
while n < 31:
    while True:
        h_list = []
        date = int(input("date:[1-30]"))
        if date < 1 or date > 30:
            print("try agin")
            continue
        hours = int(input("hours:12 ta 18"))
        if hours < 12 or hours > 18:
            print("try agin")
            continue
        shiva = 0
        for i in sum_list:
            if i[2] == date:
                if i[3] == hours:
                    print("try agin")
                    shiva += 1
        if shiva != 1:
            print("palse enter your information=")
            first_name = input("first_name=")
            last_last = input("last_name=")
            print(f'nobat shama ba nam :{first_name} va family :{last_last} dar tarikh:{date} va saat {hours} rezerv shod')
            n += 1
            h += 1
            sum_list.append([first_name, last_last, date, hours])
            print(sum_list)
    
