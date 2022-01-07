import time

# deklarasi
from random import randint

version = '5.0.5'
food = 0
uang = 0
health = 0
maxhealth = 0
strength = 0
agility = 0
intelligence = 0
datalogin = [["daffa", "123"], ["syahfei", "123"], ["fauzi", "123"], ["akbar", "123"]]


def menupertama():
    print("silakan pilih pilihan dibawah")
    print("1. Register")
    print("2. Login")
    print("3. cari user")
    print("4. keluar")
    inputs = input("masukkan pilihan anda : ")
    if inputs == "1":
        print("silahkan register")
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        register(username, password)
    elif inputs == "2":
        print("login")
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        login(username, password)
    elif inputs == "3":
        cariUser(datalogin, input("nama user : "))
    elif inputs == "4":
        keluar = input("apakah anda mau main (Y,N) : ")
        if keluar == "y":
            menupertama()
        elif keluar == "n":
            print("goodbye player")
            quit()
        else:
            print("salah input")
            menupertama()


def cariUser(user, cari):
    # list(map(lambda x: x if x[0] == cari else "", user))

    mapsUser = map(lambda x: x if x[0] == cari else "", user)

    #objec map adalah lazy evaluasi karena,
    #else if baru dijalkan saat dibuthkan, objecs maps masih blm menjelakan isi-nya(tidak mengetahui hasil)

    isFound = False
    for item in mapsUser:
        if item != "":
            isFound = True
            print(item[0])
    if not isFound:
        print("tidak ditemukan\n\n")
    menupertama()
    return


def register(username, password):
    global datalogin
    i = 2
    newUser = [username, password]
    if newUser not in datalogin:
        datalogin.insert(i, newUser)
    i = +1
    return menupertama()


def login(username, password):
    global datalogin
    isUserFound = False
    for temp in datalogin:
        if username == temp[0] and password == temp[1]:
            print("\n\n" + "selamat datang pemain " + temp[0])
            tingkatan()
            isUserFound = True
            break
    if not isUserFound:
        print("salah akun. \n\n")
        menupertama()


def tingkatan():
    global food
    global uang
    global health
    global maxhealth

    print("1. easy")
    print("2. medium")
    print("3. hard")
    print("4. HELL")
    pilihan = input("masukkan tingkat kesulitan : ")
    if pilihan == '1':
        food = 800
        health = 100
        maxhealth = 100
        uang = 100000
        return roles1()
    elif pilihan == '2':
        food = 400
        health = 90
        maxhealth = 100
        uang = 80000
        return roles1()
    elif pilihan == '3':
        food = 150
        health = 80
        maxhealth = 100
        uang = 60000
        return roles1()
    elif pilihan == '4':
        food = 50
        health = 70
        maxhealth = 100
        uang = 40000
        return roles1()
    else:
        print("inputan salah")
        return tingkatan()


def roles1():
    global strength
    global agility
    global intelligence
    print("kelebihan dan kekurangan strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    print("pilih roles pertama anda")
    print("1. strength")
    print("2. agility")
    print("3. intelligence")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength += 900
    elif inputs == "2":
        agility += 300
    elif inputs == "3":
        intelligence += 600
    roles2()
    return


def roles2():
    global strength
    global agility
    global intelligence
    print("kelebihan dan kekurangan strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    print("pilih roles kedua anda")
    print("1. strength")
    print("2. agility")
    print("3. intelligence")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength += 900
    elif inputs == "2":
        agility += 300
    elif inputs == "3":
        intelligence += 600
    roles3()
    return


def roles3():
    global strength
    global agility
    global intelligence
    print("kelebihan dan kekurangan strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("kelebihan dan kekurangan intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    print("pilih roles ketiga anda")
    print("1. strength")
    print("2. agility")
    print("3. intelligence")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength += 900
    elif inputs == "2":
        agility += 300
    elif inputs == "3":
        intelligence += 600
    karakter()
    return


def karakter():
    introduction1()


def status1():
    global uang
    global strength
    global agility
    global intelligence
    global food
    print('')
    print('food : ', food)
    print('uang : ', uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ', strength)
    print('agility : ', agility)
    print('intelligence : ', intelligence)
    return mainmenu1()


def status2():
    global uang
    global strength
    global agility
    global intelligence
    global food
    print('')
    print('food : ', food)
    print('uang : ', uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ', strength)
    print('agility : ', agility)
    print('intelligence : ', intelligence)
    return mainmenu2()


def status3():
    global uang
    global strength
    global agility
    global intelligence
    global food
    print('')
    print('food : ', food)
    print('uang : ', uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ', strength)
    print('agility : ', agility)
    print('intelligence : ', intelligence)
    return mainmenu3()


def memalak():
    global strength
    global agility
    global intelligence
    global uang
    global health
    print("menu untuk gangstar")
    print("1. uang sekolah SMA")
    print("2. uang pasar")
    print("3. uang judi")
    print("4. jual narkoba")
    inputs = input("masukkan skill yang mau di asah : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        health -= 10
        strength += 20
        agility += 5
        intelligence += 0
        uang -= 10000
        return mainmenu1()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        health -= 20
        strength += 20
        agility += 5
        intelligence += 0
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang/4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    elif value <= 2:
        print("kamu di tangkap polisi")
        health -= 30
        strength += 20
        agility += 5
        intelligence += 0
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang/2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    else:
        if inputs == "1":
            health -= 3
            uang += 10000
            strength += 200
            agility += 50
            intelligence += 0
            return mainmenu1()
        elif inputs == "2":
            health -= 4
            uang += 50000
            strength += 400
            agility += 100
            intelligence += 50
            return mainmenu1()
        elif inputs == "3":
            health -= 5
            uang += 100000
            strength += 600
            agility += 150
            intelligence += 200
            return mainmenu1()
        elif inputs == "4":
            strength += 800
            agility += 250
            intelligence += 300
            return narkoba()


def narkoba():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("narkoba yang mau di jual")
    print("1. ganja")
    print("2. sabu")
    print("3. morfin")
    print("4. heroin ( putaw )")
    inputs = input("masukkan pilihan anda : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 10
        uang -= 10000
        return mainmenu1()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    else:
        if inputs == "1":
            health -= 3
            uang += 10000
            return mainmenu1()
        elif inputs == "2":
            health -= 4
            uang += 20000
            return mainmenu1()
        elif inputs == "3":
            health -= 5
            uang += 30000
            return mainmenu1()
        elif inputs == "4":
            health -= 6
            uang += 40000
            return mainmenu1()


def merampok():
    global strength
    global agility
    global intelligence
    global uang
    global health
    print("menu untuk mau di curi")
    print("1. maling sendal")
    print("2. maling tv")
    print("3. maling motor")
    print("4. maling yang lain")
    inputs = input("masukkan skill yang mau di asah : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 10
        uang -= 10000
        return mainmenu2()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    else:
        if inputs == "1":
            strength += 0
            agility += 100
            intelligence += 50
            return mainmenu2()
        elif inputs == "2":
            strength += 50
            agility += 150
            intelligence += 100
            return mainmenu2()
        elif inputs == "3":
            strength += 100
            agility += 250
            intelligence += 150
            return mainmenu2()
        elif inputs == "4":
            strength += 150
            agility += 300
            intelligence += 200
            return maling()


def maling():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("barang yang mau di maling")
    print("1. Maling rice cooker")
    print("2. Maling sepatu")
    print("3. Maling helm")
    print("4. Maling AC")
    inputs = input("masukkan pilihan anda : ")
    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 10
        uang -= 10000
        return mainmenu2()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    else:
        if inputs == "1":
            health -= 3
            uang += 10000
            return mainmenu2()
        elif inputs == "2":
            health -= 4
            uang += 20000
            return mainmenu2()
        elif inputs == "3":
            health -= 5
            uang += 30000
            return mainmenu2()
        elif inputs == "4":
            health -= 6
            uang += 40000
            return mainmenu2()


def hacker():
    global strength
    global agility
    global intelligence
    global uang
    global health
    print("menu untuk hacker")
    print("1. hack wifi")
    print("2. hack hp")
    print("3. nyuri data base KTP")
    print("4. hack atm")
    inputs = input("masukkan skill yang mau di asah : ")\

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 10
        uang -= 10000
        return mainmenu3()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    else:
        if inputs == "1":
            strength += 0
            agility += 50
            intelligence += 100
            return mainmenu3()
        elif inputs == "2":
            strength += 0
            agility += 100
            intelligence += 150
            return mainmenu3()
        elif inputs == "3":
            strength += 0
            agility += 150
            intelligence += 200
            return mainmenu3()
        elif inputs == "4":
            strength += 100
            agility += 200
            intelligence += 300
            return atm()


def atm():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("atm yang mau di serang")
    print("1. atm BRI")
    print("2. atm BNI")
    print("3. atm BCA")
    print("4. atm Mandiri")
    inputs = input("masukkan pilihan anda : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 10
        uang -= 10000
        return mainmenu3()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    else:
        if inputs == "1":
            health -= 3
            uang += 10000
            return mainmenu3()
        elif inputs == "2":
            health -= 4
            uang += 20000
            return mainmenu3()
        elif inputs == "3":
            health -= 5
            uang += 30000
            return mainmenu3()
        elif inputs == "4":
            health -= 6
            uang += 40000
            return mainmenu3()


def daerahdikuasai():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("daerah yang mau di gangstar")
    print("1. kuasain tirto utomo")
    print("2. kuasain sukun")
    print("3. kuasain suhat")
    print("4. kuasain ijen")
    inputs = input("masukkan pilihan anda : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 10
        uang -= 10000
        return mainmenu1()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 20
        agility += 5
        intelligence += 0
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu1()
    else:
        if inputs == "1":
            health -= 10
            print("health kamu berkurang karena di kejar sama polisi dan saingan gang mu")
            uang += 10000
            print("uang yang di peroleh 10000")
            return mainmenu1()
        elif inputs == "2":
            health -= 20
            print("health kamu berkurang karena di kejar sama polisi dan saingan gang mu")
            uang += 13000
            print("uang yang di peroleh 13000")
            return mainmenu1()
        elif inputs == "3":
            health -= 25
            print("health kamu berkurang karena di kejar sama polisi dan saingan gang mu")
            uang += 15000
            print("uang yang di peroleh 15000")
            return mainmenu1()
        elif inputs == "4":
            health -= 30
            print("health kamu berkurang karena di kejar sama polisi dan saingan gang mu")
            uang += 20000
            print("uang yang di peroleh 20000")
            return mainmenu1()



def daerahmaling():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("daerah yang mau di rampok")
    print("1. perumahan tirto utomo")
    print("2. perumahan sukun")
    print("3. perumahan suhat")
    print("4. perumahan ijen")
    inputs = input("masukkan pilihan anda : ")

    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 10
        uang -= 10000
        return mainmenu2()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 20
        intelligence += 5
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu2()
    else:
        if inputs == "1":
            health -= 10
            print("health kamu berkurang karena di kejar sama satpam dan warga sekitar daerah tirto utomo dan sempat di pukul")
            uang += 10000
            print("uang yang di peroleh 10000")
            return mainmenu2()
        elif inputs == "2":
            health -= 20
            print("health kamu berkurang karena di kejar sama satpam dan warga sekitar daerah sukun dan sempat di pukul")
            uang += 13000
            print("uang yang di peroleh 13000")
            return mainmenu2()
        elif inputs == "3":
            health -= 25
            print("health kamu berkurang karena di kejar sama satpam dan warga sekitar daerah suhat dan sempat di pukul")
            uang += 15000
            print("uang yang di peroleh 15000")
            return mainmenu2()
        elif inputs == "4":
            health -= 30
            print("health kamu berkurang karena di kejar sama satpam dan warga sekitar daerah ijen dan sempat di pukul")
            uang += 20000
            print("uang yang di peroleh 20000")
            return mainmenu2()


def daerahhacker():
    global health
    global uang
    global strength
    global agility
    global intelligence
    print("daerah yang mau di serang")
    print("1. serang cyber malang")
    print("2. serang cyber batu")
    print("3. serang cyber lamongan")
    print("4. serang cyber surabaya")
    inputs = input("masukkan pilihan anda : ")
    value = randint(0, 10)

    if value <= 4:
        print("Akasi gagal\nada warga yg memergoki kamu\ntapi kamu berhasil lari.")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 10
        uang -= 10000
        return mainmenu3()
    elif value <= 3:
        print("kamu di jebak sama teman mu dan kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 20
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 4
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    elif value <= 2:
        print("kamu di tangkap polisi")
        strength += 5
        agility += 10
        intelligence += 20
        health -= 30
        if uang >= 100000:
            print("apa kamu mau keluar dari penjara?")
            pilihan = input("apa kah mau di ulangin : ")
            if pilihan == "y":
                uang -= uang / 2
                return mainmenu1()
            elif pilihan == "n":
                print("kamu memilih di penjara karena kamu pelit")
                quit()
        else:
            print("uang mu habis dan kamu di penjara selama nya")
            quit()
        return mainmenu3()
    else:
        if inputs == "1":
            health -= 10
            print("health kamu berkurang karena di kejar sama polisi")
            uang += 10000
            print("uang yang di peroleh 10000")
            return mainmenu3()
        elif inputs == "2":
            health -= 20
            print("health kamu berkurang karena di kejar sama polisi")
            uang += 13000
            print("uang yang di peroleh 13000")
            return mainmenu3()
        elif inputs == "3":
            health -= 25
            print("health kamu berkurang karena di kejar sama polisi")
            uang += 15000
            print("uang yang di peroleh 15000")
            return mainmenu3()
        elif inputs == "4":
            health -= 30
            print("health kamu berkurang karena di kejar sama polisi")
            uang += 20000
            print("uang yang di peroleh 20000")
            return mainmenu3()


def makanan1():
    global food
    global uang
    global strength
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        strength += 10
        food += 4
        uang -= 70000
        return mainmenu1()
    elif inputs == "2":
        strength += 8
        food += 3
        uang -= 50000
        return mainmenu1()
    elif inputs == "3":
        strength += 4
        food += 1
        uang -= 6000
        return mainmenu1()
    elif inputs == "4":
        strength += 6
        food += 2
        uang -= 12000
        return mainmenu1()


def makanan2():
    global food
    global uang
    global agility
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        agility += 10
        food += 4
        uang -= 70000
        return mainmenu2()
    elif inputs == "2":
        agility += 8
        food += 3
        uang -= 50000
        return mainmenu2()
    elif inputs == "3":
        agility += 4
        food += 1
        uang -= 6000
        return mainmenu2()
    elif inputs == "4":
        agility += 6
        food += 2
        uang -= 12000
        return mainmenu2()


def makanan3():
    global food
    global uang
    global intelligence
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        intelligence += 10
        food += 4
        uang -= 70000
        return mainmenu3()
    elif inputs == "2":
        intelligence += 8
        food += 3
        uang -= 50000
        return mainmenu3()
    elif inputs == "3":
        intelligence += 4
        food += 1
        uang -= 6000
        return mainmenu3()
    elif inputs == "4":
        intelligence += 6
        food += 2
        uang -= 12000
        return mainmenu3()


def rules(func):
    def warper():  # closur
        pilihan = func()  # high order
        print("rules game")
        print("1. Bila Uang Yang Dimiliki Kurang Dari 0 Maka Anda Kalah")
        print("2. Cerita Akan Ditentukan Setelah Memilih Roles (Penting!!)")
        print("3. Setiap Hari Karakter Akan Kehilang Stat Food, Dan Ketika Food Jatuh Ke 0 Maka Cerita Akan Gagal")
        print("wajib di baca !!!")
        if pilihan == "1":
            mainmenu1()
        elif pilihan == "2":
            mainmenu2()
        elif pilihan == "3":
            mainmenu3()

    return warper


@rules
def introduction1():
    print("pilih tipe karakter yang anda minatin : ")
    print("1. strangth")
    print("2. agility")
    print("3. intelgenent")
    inputs = input("masukkan pilihan karakter anda : ")

    print("sabar")
    print("loading ...")
    time.sleep(0.5)
    print('versi : ' + version)
    time.sleep(1)
    print("game sudah di stabilkan ")

    if inputs == "1":
        print("selamat datang player ")
        time.sleep(1.5)
        print("Gangster Memfokuskan Kekuatan Kamu Ke Strength. Petarung Jarak Dekat Yang Akan Menghancurkan Lawannya Dengan Tubuhnya.")
        time.sleep(1.5)
        print("Pertarungan Jarak Dekat Adalah Specialismu Dan Memalak Adalah Kegiatan Harianmu.")
        time.sleep(1.5)
        print("=====================================================================================")
        time.sleep(5.0)
    if inputs == "2":
        print("selamat datang player")
        time.sleep(1.5)
        print("Pencuri Memfokuskan Kekuatan Kamu Ke Agility. Membuatmu Semakin Cepat Dan Lincah.")
        time.sleep(1.5)
        print("Dengan Kelincahanmu Kamu Bisa Mencuri Dengan Mudah Karena Tidak Ada Yang Bisa Mengejarmu.")
        time.sleep(1.5)
        print("=====================================================================================")
        time.sleep(5.0)
    if inputs == "3":
        print("selamat datang player")
        time.sleep(1.5)
        print("Hacker Memfokuskan Kemampuanmu Pada Intelligence. Membuatmu Ahli Dalam Perkomputeran.")
        time.sleep(1.5)
        print("Dengan Keahlianmu Itu Kamu Bisa Dengan Mudah Menghack Suatu daerah Atau Mencari Informasi Yang Kamu Inginkan Di Internet...")
        time.sleep(1.5)
        print("=====================================================================================")
        time.sleep(5.0)
    return inputs


def mainmenu1():
    global uang
    global food
    global health
    print("1. memalak")
    print("2. menguasai daerah")
    print("3. beli makanan")
    print("4. ngecek status")
    print("5. keluar")
    print("6. tentang game")
    print('versi :' + version)
    while food > 0 and health > 0 and uang > 0:
        inputs = input("masukkan pilihan : ")
        if inputs == "1":
            memalak()
        elif inputs == "2":
            daerahdikuasai()
        elif inputs == "3":
            makanan1()
        elif inputs == "4":
            status1()
        elif inputs == "5":
            quit()
        elif inputs == "6":
            print("tentang game : ")
            time.sleep(1.5)
            print("nama game : indo pride")
            time.sleep(2.0)
            print('versi : ' + version)
            time.sleep(1.5)
            print('Nama Pembuat 1 : Muhammad Daffa Atthariq')
            time.sleep(1.5)
            print('NIM Pembuat 1 : 201910370311132')
            time.sleep(1.5)
            print('Ketua pembuat game sekaligus membuat cerita')
            time.sleep(1.5)
            print('Nama Pembuat 2 : Nur Syahfei')
            time.sleep(1.5)
            print('NIM Pembuat 2 : 201910370311109')
            time.sleep(1.5)
            print('Anggota membuat fitur')
            time.sleep(1.5)
            print('Nama Pembuat 3 : Rizky Ari Fauzi Hidayat')
            time.sleep(1.5)
            print('NIM Pembuat 3 : 2019103703111069')
            time.sleep(1.5)
            print('Anggota membuat laporan')
            time.sleep(1.5)
            print('Nama Pembuat 4 : Akbar Nur Habibi')
            time.sleep(1.5)
            print('NIM Pembuat 4 : 201910370311146')
            time.sleep(1.5)
            print('Anggota membuat cerita')
            time.sleep(1.5)
            pilihan = input("apakah anda mau main (Y,N) : ")
            if pilihan == "y":
                menupertama()
            if pilihan == "n":
                quit()
            else:
                print("salah input")
                return mainmenu1()

    if uang >= 110000:
        if uang <= 110000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu1()
        if uang <= 150000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu1()
        if uang <= 180000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu1()
        print("uang kamu sudah terlalu banyak kamu harus balik")
        time.sleep(1.5)
        print("kamu sudah balik ke kampung dengan terpaksa karena uang kamu terlalu banyak")
        quit()

    if food <= 0:
        print("challenge gagal")
        pilihan = input("apa kah mau di ulangin : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()

    if health <= 0:
        print("kamu sangat bar-bar")
        print("game over darah kamu habis")
        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()


def mainmenu2():
    global uang
    global food
    global health
    print("1. mencuri barang rumah orang")
    print("2. daerah yang mau di rampok")
    print("3. beli makanan")
    print("4. ngecek status")
    print("5. keluar")
    print("6. tentang game")
    print('versi :' + version)
    inputs = input("masukkan pilihan : ")
    while food > 0 and health > 0 and uang > 0:
        if inputs == "1":
            merampok()
        elif inputs == "2":
            daerahmaling()
        elif inputs == "3":
            makanan2()
        elif inputs == "4":
            status2()
        elif inputs == "5":
            quit()
        elif inputs == "6":
            print("tentang game : ")
            time.sleep(1.5)
            print("nama game : indo pride")
            time.sleep(2.0)
            print('versi : ' + version)
            time.sleep(1.5)
            print('Nama Pembuat 1 : Muhammad Daffa Atthariq')
            time.sleep(1.5)
            print('NIM Pembuat 1 : 201910370311132')
            time.sleep(1.5)
            print('Ketua pembuat game sekaligus membuat cerita')
            time.sleep(1.5)
            print('Nama Pembuat 2 : Nur Syahfei')
            time.sleep(1.5)
            print('NIM Pembuat 2 : 201910370311109')
            time.sleep(1.5)
            print('Anggota membuat fitur')
            time.sleep(1.5)
            print('Nama Pembuat 3 : Rizky Ari Fauzi Hidayat')
            time.sleep(1.5)
            print('NIM Pembuat 3 : 2019103703111069')
            time.sleep(1.5)
            print('Anggota membuat laporan')
            time.sleep(1.5)
            print('Nama Pembuat 4 : Akbar Nur Habibi')
            time.sleep(1.5)
            print('NIM Pembuat 4 : 201910370311146')
            time.sleep(1.5)
            print('Anggota membuat cerita')
            time.sleep(1.5)
            pilihan = input("apakah anda mau main (Y,N) : ")
            if pilihan == "y":
                menupertama()
            if pilihan == "n":
                quit()
            else:
                print("salah input")
                return mainmenu2()

    if uang >= 200000:
        if uang <= 110000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu2()
        if uang <= 150000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu2()
        if uang <= 180000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu2()
        print("uang kamu sudah terlalu banyak kamu harus balik")
        time.sleep(1.5)
        print("kamu sudah balik ke kampung dengan terpaksa karena uang kamu terlalu banyak")
        quit()

    if food <= 0:
        print("challenge gagal")
        pilihan = input("apa kah mau di ulangin : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()

    if health <= 0:
        print("kamu sangat bar-bar")
        print("game over darah kamu habis")
        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()


def mainmenu3():
    global uang
    global food
    global health
    print("1. mengasah skill hacker")
    print("2. memilih daerah yang mau di serang")
    print("3. beli makanan")
    print("4. ngecek status")
    print("5. keluar")
    print("6. tentang game")
    print('versi :' + version)
    inputs = input("masukkan pilihan : ")
    while food > 0 and health > 0 and uang > 0:
        if inputs == "1":
            hacker()
        elif inputs == "2":
            daerahhacker()
        elif inputs == "3":
            makanan3()
        elif inputs == "4":
            status3()
        elif inputs == "5":
            quit()
        elif inputs == "6":
            print("tentang game : ")
            time.sleep(1.5)
            print("nama game : indo pride")
            time.sleep(2.0)
            print('versi : ' + version)
            time.sleep(1.5)
            print('Nama Pembuat 1 : Muhammad Daffa Atthariq')
            time.sleep(1.5)
            print('NIM Pembuat 1 : 201910370311132')
            time.sleep(1.5)
            print('Ketua pembuat game sekaligus membuat cerita')
            time.sleep(1.5)
            print('Nama Pembuat 2 : Nur Syahfei')
            time.sleep(1.5)
            print('NIM Pembuat 2 : 201910370311109')
            time.sleep(1.5)
            print('Anggota membuat fitur')
            time.sleep(1.5)
            print('Nama Pembuat 3 : Rizky Ari Fauzi Hidayat')
            time.sleep(1.5)
            print('NIM Pembuat 3 : 2019103703111069')
            time.sleep(1.5)
            print('Anggota membuat laporan')
            time.sleep(1.5)
            print('Nama Pembuat 4 : Akbar Nur Habibi')
            time.sleep(1.5)
            print('NIM Pembuat 4 : 201910370311146')
            time.sleep(1.5)
            print('Anggota membuat cerita')
            time.sleep(1.5)
            pilihan = input("apakah anda mau main (Y,N) : ")
            if pilihan == "y":
                menupertama()
            if pilihan == "n":
                quit()
            else:
                print("salah input")
                return mainmenu3()
    if uang >= 200000:
        if uang <= 110000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu3()
        if uang <= 150000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu3()
        if uang <= 180000:
            print("apakah kamu mau balik ke kota asal kamu")
            print("jika iya pilih tombol Y, jika kamu masih tetap di malang tekan N")
            pilihan = input("masukkan pilihan anda : ")
            if pilihan == "y":
                quit()
            elif pilihan == "n":
                return mainmenu3()
        print("uang kamu sudah terlalu banyak kamu harus balik")
        time.sleep(1.5)
        print("kamu sudah balik ke kampung dengan terpaksa karena uang kamu terlalu banyak")
        quit()

    if food <= 0:
        print("challenge gagal")
        pilihan = input("apa kah mau di ulangin : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()

    if health <= 0:
        print("kamu sangat bar-bar")
        print("game over darah kamu habis")
        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()


def start():  # pure funcion
    print("selamat datang di game indo pride")
    return


start()
menupertama()
