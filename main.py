import time
import random

#deklarasi
version = '0.0.1'
playername = ''
password = ''
food = 0
uang = 0
health = 0
maxhealth = 0
strength = 0
agility = 0
intelligence = 0
food2 = 0
random_hari = 0
tahun = 0
datemonth = 'januari'
bulan = 1
hari = 1
totalhari = 0
bulan_31 = [1,3,5,7,8,10,12]
event_k = random.randint(1,3)
datalogin = [["daffa", "123"], ["syahfei", "123"], ["fauzi", "123"], ["akbar", "123"]]

def menupertama():
    print("silakan pilih pilihan dibawah")
    print("1. Register")
    print("2. Login")
    print("3. keluar")
    inputs = input("masukkan pilihan anda : ")
    if inputs == "1":
        print("silahkan register")
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        register(username,password)
    elif inputs == "2":
        print("login")
        username = input("masukkan username : ")
        password = input("masukkan password : ")
        login(username,password)
    elif inputs == "3":
        keluar = input("apakah anda mau main (Y,N) : ")
        if keluar == "y":
            menupertama()
        elif keluar == "n":
            print("goodbye player")
            quit()
        else:
            print("salah input")
            menupertama()

def register(username,password):
    global datalogin
    i = 2
    datalogin.insert(i,[username,password])
    i = +1
    return menupertama()

def login(username,password):
    global datalogin
    while True:

        for x in datalogin:
            temp = x
            for temp in datalogin:
                if username == temp[0] and password == temp[1]:
                    print("\n\n" + "selamat datang pemain " + temp[0])
                    tingkatan()
                    break
            print("salah akun. \n\n")
            menupertama()
            break

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
        return roles2()
    elif inputs == "2":
        agility += 300
        return roles2()
    elif inputs == "3":
        intelligence += 600
        return roles2()

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
        return roles3()
    elif inputs == "2":
        agility += 300
        return roles3()
    elif inputs == "3":
        intelligence += 600
        return roles3()

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
        return karakter()
    elif inputs == "2":
        agility += 300
        return karakter()
    elif inputs == "3":
        intelligence += 600
        return karakter()

def karakter():
    print("pilih tipe karakter yang anda minatin : ")
    print("1. strangth")
    print("2. agility")
    print("3. intelgenent")
    inputs = input("masukkan pilihan karakter anda : ")
    if inputs == "1":
        return loading1()
    elif inputs == "2":
        return loading2()
    elif inputs == "3":
        return loading3()

def loading1():
    print("sabar")
    print("loading ...")
    time.sleep(0.5)
    print('versi : '+version)
    time.sleep(1)
    print("game sudah di stabilkan " + str(playername)+'')
    return introduction1()

def loading2():
    print("sabar")
    print("loading ...")
    time.sleep(0.5)
    print('versi : '+version)
    time.sleep(1)
    print("game sudah di stabilkan " + str(playername)+'')
    return introduction2()

def loading3():
    print("sabar")
    print("loading ...")
    time.sleep(0.5)
    print('versi : '+version)
    time.sleep(1)
    print("game sudah di stabilkan " + str(playername)+'')
    return introduction3()

def status1():
    global uang
    global strength
    global agility
    global intelligence
    global food
    global food2
    print('')
    print('food : ',food)
    print('uang : ',uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ',strength, '+',food2)
    print('agility : ',agility)
    print('intelligence : ',intelligence)
    return mainmenu1()

def status2():
    global uang
    global strength
    global agility
    global intelligence
    print('')
    print('food : ', food)
    print('uang : ',uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ',strength)
    print('agility : ',agility, '+',food2)
    print('intelligence : ',intelligence)
    return mainmenu2()

def status3():
    global uang
    global strength
    global agility
    global intelligence
    print('')
    print('food : ', food)
    print('uang : ',uang)
    print('health : ', health)
    print('health max : ', maxhealth)
    print('stength : ',strength)
    print('agility : ',agility)
    print('intelligence : ',intelligence, '+',food2)
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
    print("4. hasil jual narkoba")
    inputs = input("masukkan skill yang mau di asah : ")
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
    print("narkoba yang mau di jual")
    print("1. ganja")
    print("2. sabu")
    print("3. morfin")
    print("4. heroin ( putaw )")
    inputs = input("masukkan barang yang mana mau di jual : ")
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
    print("menu untuk maling")
    print("1. maling sendal")
    print("2. maling tv")
    print("3. maling motor")
    print("4. maling AC")
    inputs = input("masukkan skill yang mau di asah : ")
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
        return mainmenu2()

def hacker():
    global strength
    global agility
    global intelligence
    print("menu untuk hacker")
    print("1. hack wifi")
    print("2. hack hp")
    print("3. nyuri data base KTP")
    print("4. hack atm")
    inputs = input("masukkan skill yang mau di asah : ")
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
        return mainmenu3()

def makanan1():
    global food
    global uang
    global food2
    global strength
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        food += 4
        food2 += 50
        uang -= 70000
        return mainmenu1()
    elif inputs == "2":
        food += 3
        food2 += 30
        uang -= 50000
        return mainmenu1()
    elif inputs == "3":
        food += 1
        food2 += 10
        uang -= 6000
        return mainmenu1()
    elif inputs == "4":
        food += 2
        food2 += 20
        uang -= 12000
        return mainmenu1()

def makanan2():
    global food
    global uang
    global food2
    global agility
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        food += 4
        food2 += 50
        uang -= 70000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu2()
    elif inputs == "2":
        food += 3
        food2 += 30
        uang -= 50000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu2()
    elif inputs == "3":
        food += 1
        food2 += 10
        uang -= 6000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu2()
    elif inputs == "4":
        food += 2
        food2 += 20
        uang -= 12000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu2()

def makanan3():
    global food
    global uang
    global food2
    global intelligence
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        food += 4
        food2 += 50
        uang -= 70000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu3()
    elif inputs == "2":
        food += 3
        food2 += 30
        uang -= 50000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu3()
    elif inputs == "3":
        food += 1
        food2 += 10
        uang -= 6000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu3()
    elif inputs == "4":
        food += 2
        food2 += 20
        uang -= 12000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu3()

def next(min,max):
    global hari
    global bulan
    global bulan_31
    global random_hari
    global food
    global health
    global health_d1
    global health_d2
    global totalhari
    global event_k

    random_hari = random.randint(min,max)
    print("sudah ",random_hari,"hari berlangsung ")
    hari_min = hari
    cek_rata = hari + random_hari

    if event_k == 1:
        a_number = random.randint(1,6)
        a_health_num = random.randint(1,3)
        random_hari2_food = random.randint(5,30)
        random_hari2_hari = random.randint(1,10)
        if a_number == 1:
            print("pada waktu ini, kamu mencari mangsa")
        if a_number == 2:
            print("pada waktu ini, kamu sakit")
            health -= 1
        if a_number == 3:
            print("pada waktu ini, kamu di begal")
            food -=35
            print("kehilangan 35 kg berat badan")
        if a_number == 4:
            print("pada waktu ini, partner mu menghianat")
            totalhari += random_hari2_hari
            hari += random_hari2_hari
            print("makan waktu " + str(random_hari2_hari) + " hari buat meorginisir barang")
        if a_number == 5:
            print("pada waktu ini, kamu kena busur")
            health -=4
        if a_number == 6:
            print("pada waktu ini, jalan lagi di perbaiki, kamu terpaksa mutar lewat jalan lain")
            totalhari += random_hari2_hari
            hari += random_hari2_hari
            food -= random_hari2_food
            print("karena itu, kamu makan "+str(random_hari2_food)+" kg")
            print("makan waktu "+str(random_hari2_hari)+" hari buat istirahat")
        if a_health_num == 1:
            print("dan juga kehilangan 1 health")
            health -= 1
        food = food - random_hari2_food - random_hari2_hari*5
        hari += random_hari2_hari
        totalhari += random_hari2_hari

    cek_rata = hari + random_hari
    if health_d1 >= hari_min and health_d1 <= cek_rata:
        health -= 1
        print("kamu kehilangan 1 health")
    if health_d2 >= hari_min and health_d2 <= cek_rata:
        health -= 1
        print("kamu kehilangan 1 health")

    hari += random_hari
    totalhari += random_hari
    food = random_hari * 5

    if hari >= 30:
        if bulan not in bulan_31:
            if hari > 30 :
                hari -= 30
                bulan += 1
                health_d1 = random.randint(1,30)
                health_d2 = random.randint(1,30)
                event_k = random.randint(1,3)
            else:
                if hari > 31 :
                    hari -= 31
                    bulan += 1
                    health_d1 = random.randint(1,30)
                    health_d2 = random.randint(1,30)
                    event_k = random.randint(1,4)


def introduction1():
    print("selamat datang player ")
    time.sleep(1.5)
    print("tahun  terjadi perang saudara")
    time.sleep(1.5)
    print("terjadinya ini karena perebutan daerah")
    time.sleep(1.5)
    print("banyak sekali korban yang terkena terdampak perang")
    time.sleep(1.5)
    print("salah satu negara yang dekat terjadinya perang ini tidak terkena dampak nya")
    time.sleep(1.5)
    print("dampak perang ini mengakibatkan kurangnya makanan dan minuman")
    time.sleep(1.5)
    print("membuat masyarakat harus pindah daerah yang lebih baik")
    time.sleep(1.5)
    print("kalimantan adalah kota yang paling aman untuk di tempatin oleh masyarakat")
    time.sleep(1.5)
    print("kita akan ke kalimantan, yang dimana kota awalnya berada di " )
    time.sleep(1.5)
    print("jarak ke kalimantan ( km ) kamu harus sampai 31 desember")
    time.sleep(1.5)
    print("karena makanan dan minuman semakin tipis dan akan ada perang selanjutnya")
    time.sleep(1.5)
    print("tetapi jalan tidak selalu mulus")
    time.sleep(1.5)
    print("setiap hari kamu bisa kehilangan makanan dan darah. kamu bisa berburu dan istirahat")
    time.sleep(1.5)
    print("=====================================================================================")
    rules()
    time.sleep(5.0)
    return mainmenu1()

def introduction2():
    print("selamat datang player")
    time.sleep(1.5)
    print("tahun terjadi perang saudara")
    time.sleep(1.5)
    print("terjadinya ini karena perebutan daerah")
    time.sleep(1.5)
    print("banyak sekali korban yang terkena terdampak perang")
    time.sleep(1.5)
    print("salah satu negara yang dekat terjadinya perang ini tidak terkena dampak nya")
    time.sleep(1.5)
    print("dampak perang ini mengakibatkan kurangnya makanan dan minuman")
    time.sleep(1.5)
    print("membuat masyarakat harus pindah daerah yang lebih baik")
    time.sleep(1.5)
    print("kalimantan adalah kota yang paling aman untuk di tempatin oleh masyarakat")
    time.sleep(1.5)
    print("kita akan ke kalimantan, yang dimana kota awalnya berada di ")
    time.sleep(1.5)
    print("jarak ke kalimantan ( km ) kamu harus sampai 31 desember")
    time.sleep(1.5)
    print("karena makanan dan minuman semakin tipis dan akan ada perang selanjutnya")
    time.sleep(1.5)
    print("tetapi jalan tidak selalu mulus")
    time.sleep(1.5)
    print("setiap hari kamu bisa kehilangan makanan dan darah. kamu bisa berburu dan istirahat")
    time.sleep(1.5)
    print("=====================================================================================")
    rules()
    time.sleep(5.0)
    return mainmenu2()

def introduction3():
    print("selamat datang player")
    time.sleep(1.5)
    print("tahun terjadi perang saudara")
    time.sleep(1.5)
    print("terjadinya ini karena perebutan daerah")
    time.sleep(1.5)
    print("banyak sekali korban yang terkena terdampak perang")
    time.sleep(1.5)
    print("salah satu negara yang dekat terjadinya perang ini tidak terkena dampak nya")
    time.sleep(1.5)
    print("dampak perang ini mengakibatkan kurangnya makanan dan minuman")
    time.sleep(1.5)
    print("membuat masyarakat harus pindah daerah yang lebih baik")
    time.sleep(1.5)
    print("kalimantan adalah kota yang paling aman untuk di tempatin oleh masyarakat")
    time.sleep(1.5)
    print("kita akan ke kalimantan, yang dimana kota awalnya berada di ")
    time.sleep(1.5)
    print("jarak ke kalimantan ( km ) kamu harus sampai 31 desember")
    time.sleep(1.5)
    print("karena makanan dan minuman semakin tipis dan akan ada perang selanjutnya")
    time.sleep(1.5)
    print("tetapi jalan tidak selalu mulus")
    time.sleep(1.5)
    print("setiap hari kamu bisa kehilangan makanan dan darah. kamu bisa berburu dan istirahat")
    time.sleep(1.5)
    print("=====================================================================================")
    rules()
    time.sleep(5.0)
    return mainmenu3()

def rules():
    print("rules game")
    print("1. Bila Uang Yang Dimiliki Kurang Dari 0 Maka Anda Kalah")
    print("2. Cerita Akan Ditentukan Setelah Memilih Roles (Penting!!)")
    print("3. Setiap Hari Karakter Akan Kehilang Stat Food, Dan Ketika Food Jatuh Ke 0 Maka Cerita Akan Gagal")
    print("wajib di baca !!!")

def mainmenu1():
    global uang
    global food
    global food2
    global health
    global bulan
    print("1. memalak")
    # print("2. bisa masuk join gangstar")
    print("3. menguasai daerah")
    print("4. beli makanan")
    print("5. ngecek status")
    print("6. keluar")
    print("7. tentang game")
    print('versi :' + version)
    while food > 0 and health > 0 and uang > 0 and bulan < 13:
        inputs = input("masukkan pilihan : ")
        if inputs == "1":
            memalak()
        # elif inputs == "2":
        #     return 0
        elif inputs == "3":
            health -= 5
            print("health kamu berkurang karena kamu menguasain daerah")
            uang += 10000
            print("uang yang di peroleh 10000")
            return mainmenu1()
        elif inputs == "4":
            makanan1()
        elif inputs == "5":
            status1()
        elif inputs == "6":
            quit()
        elif inputs == "7":
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
    if food <= 0:
        print("challenge gagal ")
        print("kamu mati di malang : ")
        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()

    if uang >= 200000:
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

    if uang <= 0:
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

    if bulan >= 13:
        print("game over darah kamu habis")
        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        elif pilihan == "n":
            quit()

def mainmenu2():
    global food
    global uang
    print("1. merampok rumah orang")
    print("2. daerah yang mau di rampok")
    print("3. beli makanan")
    print("4. hasil curian")
    print("5. ngecek status")
    print("6. keluar")
    print("7. tentang game")
    print('versi :' + version)
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        merampok()
    elif inputs == "2":
        return 0
    elif inputs == "3":
        return 0
    elif inputs == "4":
        print("uang saat ini", uang)
        return mainmenu2()
    elif inputs == "5":
        status2()
    elif inputs == "6":
        quit()
    elif inputs == "7":
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
def mainmenu3():
    global food
    global uang
    print("1. mengasah skill hacker")
    print("2. memilih daerah yang mau di serang")
    print("3. beli makanan")
    print("4. mengambil hasil hacker")
    print("5. ngecek status")
    print("6. keluar")
    print("7. tentang game")
    print('versi :' + version)
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        hacker()
    elif inputs == "2":
        return 0
    elif inputs == "3":
        return 0
    elif inputs == "4":
        print("uang saat ini", uang)
        return mainmenu3()
    elif inputs == "5":
        status3()
    elif inputs == "6":
        quit()
    elif inputs == "7":
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


def start():
    print("selamat datang di game indo pride")
    return menupertama()

start()
