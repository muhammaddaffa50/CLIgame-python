import time

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
        health = 10
        maxhealth = 10
        uang = 100000
        return roles1()
    elif pilihan == '2':
        food = 400
        health = 9
        maxhealth = 7
        uang = 80000
        return roles1()
    elif pilihan == '3':
        food = 150
        health = 6
        maxhealth = 5
        uang = 60000
        return roles1()
    elif pilihan == '4':
        food = 50
        health = 4
        maxhealth = 3
        uang = 40000
        return roles1()
    elif playername == 'daffa' and pilihan == '5':
        food = 99999
        health = 99999
        maxhealth = 99999
        uang = 99999
        print("wahhh cheater parah sih noob")
        return roles1()
    else:
        print("inputan salah")
        return tingkatan()

def roles1():
    global strength
    global agility
    global intelligence
    print("pilih roles pertama anda")
    print("1. strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("2. agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("3. intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength = 900
        return roles2()
    elif inputs == "2":
        agility = 300
        return roles2()
    elif inputs == "3":
        intelligence = 600
        return roles2()

def roles2():
    global strength
    global agility
    global intelligence
    print("pilih roles kedua anda")
    print("1. strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("2. agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("3. intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength = 900
        return roles3()
    elif inputs == "2":
        agility = 300
        return roles3()
    elif inputs == "3":
        intelligence = 600
        return roles3()

def roles3():
    global strength
    global agility
    global intelligence
    print("pilih roles ketiga anda")
    print("1. strength")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang kuat")
    print("2. menaikan skill fisik lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik lebih lama")
    print("=========================================")
    print("2. agility")
    print("=========================================")
    print("keuntungan : ")
    print("1. Tubuh yang lincah")
    print("2. menaikan skill lincah lebih cepat")
    print("kekurangan : ")
    print("1. menaikan skill selain lincah lebih lama")
    print("=========================================")
    print("3. intelligence")
    print("=========================================")
    print("keuntungan : ")
    print("1. punya otak yang pintar")
    print("2. menaikan skill otak ")
    print("kekurangan : ")
    print("1. menaikan skill selain fisik dan lincah lebih lama")
    print("=========================================")
    inputs = input("masukkan pilihan roles anda : ")
    if inputs == "1":
        strength = 900
        return karakter()
    elif inputs == "2":
        agility = 300
        return karakter()
    elif inputs == "3":
        intelligence = 600
        return karakter()

def karakter():
    print("pilih tipe karakter yang anda minatin : ")
    print("1. strangth")
    print("2. agility")
    print("3. intelgenent")
    inputs = input("masukkan pilihan karakter anda : ")
    if inputs == "1":
        return kekuatan()
    elif inputs == "2":
        return kelincahan()
    elif inputs == "3":
        return kecerdasan()

def kekuatan():
    print("pilih karakter agility anda")
    print("1. gangster")
    print("2. bodyguards")
    print("3. coach")
    print("4. polisi")
    inputs = input("masukkan karater yang anda minatin : ")
    if inputs == "1":
        return loading1()
    elif inputs == "2":
        return loading1()
    elif inputs == "3":
        return loading1()
    elif inputs == "4":
        return loading1()
    else:
        print("salah input")
        kekuatan()

def kelincahan():
    print("pilih karakter strangth anda")
    print("1. Thief ( pencuri )")
    print("2. Assasin")
    print("3. Hidden Bodyguards")
    inputs = input("masukkan karater yang anda minatin : ")
    if inputs == "1":
        return loading2()
    elif inputs == "2":
        return loading2()
    elif inputs == "3":
        return loading2()
    else:
        print("salah input")
        kelincahan()

def kecerdasan():
    print("pilih karakter intelegenet anda")
    print("1. IT")
    print("2. Hacker")
    print("3. Pilisi ( intelligence Departement )")
    inputs = input("masukkan karater yang anda minatin : ")
    if inputs == "1":
        return loading3()
    elif inputs == "2":
        return loading3()
    elif inputs == "3":
        return loading3()
    else:
        print("salah input")
        kecerdasan()

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
    print('stength : ',strength)
    print('agility : ',agility)
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
    print('stength : ',strength)
    print('agility : ',agility)
    print('intelligence : ',intelligence)
    return mainmenu3()

def memalak():
    global strength
    global agility
    global intelligence
    global uang
    print("menu untuk gangstar")
    print("1. uang sekolah anak-anak")
    print("2. uang pasar")
    print("3. uang judi")
    print("4. hasil jual narkoba")
    inputs = input("masukkan skill yang mau di asah : ")
    if inputs == "1":
        uang += 10000
        strength += 200
        agility += 50
        intelligence += 0
        return mainmenu1()
    elif inputs == "2":
        uang += 50000
        strength += 400
        agility += 100
        intelligence += 50
        return mainmenu1()
    elif inputs == "3":
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
    global uang
    print("narkoba yang mau di jual")
    print("1. ganja")
    print("2. sabu")
    print("3. morfin")
    print("4. heroin ( putaw )")
    inputs = input("masukkan barang yang mana mau di jual : ")
    if inputs == "1":
        uang += 10000
        return mainmenu1()
    elif inputs == "2":
        uang += 20000
        return mainmenu1()
    elif inputs == "3":
        uang += 30000
        return mainmenu1()
    elif inputs == "4":
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
    global uang
    global food
    global food2
    global strength
    print("beli makan apa :")
    print("1. pizza hut")
    print("2. burger king")
    print("3. coca cola")
    print("4. AW sarsafalila")
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        food2 += 50
        uang -= 70000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu1()
    elif inputs == "2":
        food2 += 30
        uang -= 50000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu1()
    elif inputs == "3":
        food2 += 10
        uang -= 6000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu1()
    elif inputs == "4":
        food2 += 20
        uang -= 12000
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu1()


def introduction1():
    print("selamat datang player")
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
    print("2. Cerita Akan Ditentukan Setelah Memilih Roles(Penting!!)")
    print("3. Setiap Hari Karakter Akan Kehilang Stat Food, Dan Ketika Food Jatuh Ke 0 Maka Cerita Akan Gagal")
    print("wajib di baca !!!")

def mainmenu1():
    global food
    global uang
    print("1. memalak")
    print("2. bisa masuk join gangstar")
    print("3. menguasai daerah")
    print("4. beli makanan")
    print("5. melihat hasil sumber haram")
    print("6. ngecek status")
    print("7. keluar")
    print("8. tentang game")
    print('versi :' + version)
    inputs = input("masukkan pilihan : ")
    if inputs == "1":
        memalak()
    elif inputs == "2":
        return 0
    elif inputs == "3":
        return 0
    elif inputs == "4":
        makanan1()
    elif inputs == "5":
        print("uang saat ini",uang)
        if uang <= 0:
            print("Challange gagal\n")
            return
        return mainmenu1()
    elif inputs == "6":
        status1()
    elif inputs == "7":
        quit()
    elif inputs == "8":
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
