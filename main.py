import random
import time
import os
import getpass

#deklarasi
version = '0.0.1'
food = 0
health = 0
maxhealth = 0
jarak = 0
playername = ''
tahun = 0
datemonth = 'november'
bulan = 1
jarakgerakplayer = 0
hari = 1
totalhari = 0
bulan_31 = [1,3,5,7,8,10,12]
random_hari = 0
health_d1 = random.randint(1,31)
health_d2 = random.randint(1,31)
jalan_total = 0
istrahat_total = 0
berburu_total = 0
status_total = 0
event_k = random.randint(1,3)
strength = 0
agility = 0
intelligent = 0

def tplayer():
    global playername
    global password
    playername = input("input nama anda : ")
    password = input("input password anda : ")
    if playername == "daffa" and password == "wanted":
        print("welcome daffa")
        return years()
    elif playername == "syahfei" and password == "123":
        print("welcome fei")
        return years()
    elif playername == "fauzi" and password == "123":
        print("welcome fauzi")
    elif playername == "akbar" and password == "123":
        print("welcome akbar")
        return years()
    else:
        print("welcome to tawuran game")
        return years()

def years():
    global tahun
    tahun = input("masukkan tahun dimulainya perjalanan : ")
    if tahun.isdigit():
        return_num = 0
    else:
        return_num = 1
    while return_num == 1:
        print("error, bro")
        tahun = input("masukkan tahun dimulainya perjalanan : ")
        if tahun.isdigit():
            return_num = 0
        else:
            return_num = 1

    tahun = int(tahun)
    return difficulty()

def difficulty():
    global food
    global health
    global maxhealth
    global jarak

    print("1. easy")
    print("2. medium")
    print("3. hard")
    print("4. very hard")
    pilihan = input("masukkan tingkat kesulitan : ")
    if pilihan == '1':
        food = 800
        health = 10
        maxhealth = 10
        jarak = 2170
        return roles1()
    elif pilihan == '2':
        food = 400
        health = 9
        maxhealth = 7
        jarak = 2400
        return roles1()
    elif pilihan == '3':
        food = 200
        health = 6
        maxhealth = 5
        jarak = 3300
        return roles1()
    elif pilihan == '4':
        food = 50
        health = 4
        maxhealth = 3
        jarak = 3500
        return roles1()
    elif playername == 'daffa' and pilihan == '5':
        food = 99999
        health = 99999
        maxhealth = 99999
        jarak = 99999
        print("wahhh cheater parah sih noob")
        return roles1()
    else:
        print("inputan salah")
        return difficulty()

def loading():
    print("sabar")
    print("loading ...")
    time.sleep(0.5)
    print('versi : '+version)
    time.sleep(1)
    print("game sudah di stabilkan " + str(playername)+'')
    return introduction()

def roles1():
    global strength
    global agility
    global intelligent
    print("1. strength")
    print("2. agility")
    print("3. intelligent")
    pilihan = input("masukkan roles : ")
    if pilihan == '1':
        strength = 800
        return roles2()
    elif pilihan == '2':
        agility = 200
        return roles2()
    elif pilihan == '3':
        intelligent = 100
        return roles2()

def roles2():
    global strength
    global agility
    global intelligent
    print("1. strength")
    print("2. agility")
    print("3. intelligent")
    pilihan = input("masukkan roles : ")
    if pilihan == '1':
        strength += 800
        return roles3()
    elif pilihan == '2':
        agility += 200
        return roles3()
    elif pilihan == '3':
        intelligent += 100
        return roles3()

def roles3():
    global strength
    global agility
    global intelligent
    print("1. strength")
    print("2. agility")
    print("3. intelligent")
    pilihan = input("masukkan roles : ")
    if pilihan == '1':
        strength += 800
        return loading()
    elif pilihan == '2':
        agility += 200
        return loading()
    elif pilihan == '3':
        intelligent += 100
        return loading()

def ddatemonth():
    global datemonth
    if bulan == 1:
        datemonth = 'januari'
    elif bulan == 2:
        datemonth = 'februari'
    elif bulan == 3:
        datemonth = 'maret'
    elif bulan == 4:
        datemonth = 'april'
    elif bulan == 5:
        datemonth = 'mei'
    elif bulan == 6:
        datemonth = 'juni'
    elif bulan == 7:
        datemonth = 'juli'
    elif bulan == 8:
        datemonth = 'agustus'
    elif bulan == 9:
        datemonth = 'september'
    elif bulan == 10:
        datemonth = 'oktober'
    elif bulan == 11:
        datemonth = 'november'
    elif bulan == 12:
        datemonth = 'desember'
    return datemonth

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


def jalan(jarakjalan):
    global hari
    global jalan_total
    next(4,7)
    jarakjalan = jarakjalan + random.randint(40,80)
    jalan_total += 1
    return jarakjalan

def istirahat(health):
    global hari
    global istrahat_total
    next(2,50)
    health = maxhealth
    istrahat_total += 10
    return health

def status():
    global status_total
    print('makanan : ',food,"kg")
    print('health : ',health)
    print('jarak jalan : ',jarakgerakplayer)
    print('status', str(roles1) , str(roles2), str(roles3))
    distance_left = jarak - jarakgerakplayer
    print(''+str(hari)+ " hari telah berlangsung")
    print('kamu sudah berjalan '+str(jarakgerakplayer)+" KM, masih ada "+str(distance_left)+" KM lagi")
    status_total += 1
    return mainmenu()

def berburu(berburu_food):
    global hari
    global berburu_total
    global food
    next(2,30)
    berburu_food = food + random.randint(1,600)
    print('bertambah : '+str(berburu_food)+' kg makanan')
    berburu_total += 1
    return berburu_food



def introduction():
    print("selamat datang player")
    time.sleep(1.5)
    print("kamu adalah seorang berbakat dan pandai melakukan segala hal seperti bertarung dan lain-lain")
    time.sleep(1.5)
    print("tetapi kamu ini adalah orang paling polos dan mudah di tipu")
    time.sleep(1.5)
    print("pada suatu hari kamu bertemu sama teman-teman kamu. dan teman mu menyuruh mu untuk melakukan bisnis ilegal")
    time.sleep(1.5)
    print("dan kamu langsung setuju-setuju aja tapi kamu ngak tau bisnis apa dan belum di kasih bukti oleh teman-teman kamu")
    time.sleep(1.5)
    print("teman kamu menyuruh kamu pergi kemalang untuk melakukan bisnis ilegal ini dan diberi uang tiket")
    time.sleep(1.5)
    print("teman kamu menyuruh kamu datang harus tanggal 31 desember")
    time.sleep(1.5)
    print("dan kamu mikir jarak dari tarakan ke malang itu ("+str(jarak)+"km) tapi karena sudah di beri uang saku sama tiket keluar kota siapa yang nolak")
    time.sleep(1.5)
    print("btw ini mah bukan polos lagi sih Charakter nya melainkan tulul aowkawokawokawok")
    time.sleep(1.5)
    print("")
    print("1. cari kos")
    print("2. istirahat")
    print("3. memalak")
    print("4. cek status")
    print("5. cek diri")
    print("6. keluar")
    print("7. tentang game")
    print('versi :' + version)
    return mainmenu()

def mainmenu():
    global jarakgerakplayer
    global food
    global health

    while jarakgerakplayer < jarak and food > 0 and health > 0 and bulan < 13:
        ddatemonth()
        if food <= 10:
            print("hati-hati kamu hanya" +str(food)+ "kg makan")
            print("kamu harus memalak")
        if health <= 1:
            print("hati-hati kamu hanya"+str(health)+"health sekarang")
            print("kamu harus istirahat")
        print(str(playername)+" sekarang "+datemonth+' '+str(hari)+' '+str(tahun)+ " dan kamu berjalan "+str(jarakgerakplayer))
        pilihan = input("masukkan pilihan : ")
        if pilihan == '1':
            jarakgerakplayer = jalan(jarakgerakplayer)
        elif pilihan == '2':
            if health < maxhealth:
                print("kamu mendapat kan 1 health")
                health = istirahat(maxhealth)
            if health >= maxhealth:
                print("health kamu penuh, maximum health mu " + str(maxhealth)+ " !")
        elif pilihan == '3':
            food = berburu(food)
        elif pilihan == '4':
            status()
        elif pilihan == '5':
            print('1, jalan : 40-80 km dan menghabiskan waktu 4-7 hari')
            print('2. istirahat : menambah health 1-5 dan menghabiskan waktu 2-5 hari')
            print('3. memalak : menambah 100 kg makanan menghabiskan 2-5 hari')
            print('4. status : list makanan, health, jarak jalan, and hari')
            print('5. bantuan : list pilihan')
            print('6. keluar : keluar game')
            print('7. tentang : deskripsi game')
        elif pilihan == '6':
            quit_pilihan = input("apakah kamu yakin keluar? (Y,N) : ")
            if quit_pilihan == 'y':
                print('selamat tidur')
                break
        elif pilihan == 'bunuhdiri':
            quit_pilihan2 = input("yakin lu bunuh diri gara gara ke polosan mu (Y,N) : ")
            if quit_pilihan2 == 'y':
                print("game over")
                break
        elif pilihan == '7':
            print("tentang game : ")
            time.sleep(0.1)
            print("nama game : tawuran")
            time.sleep(0.5)
            print('versi : '+version)
            time.sleep(0.1)
            print('nama pembuat 1 : Muhammad Daffa Atthariq')
            time.sleep(0.1)
            print('nama pembuat 2 : nur syahfei')
            time.sleep(0.1)
            print('nama pembuat 3 : rizky fauzi')
            time.sleep(0.1)
            print('nama pembuat 4 : akbar nur habibi')
        else:
            print("salah input")

    if jarakgerakplayer >= jarak:
        print("selamat baru sampai di malang ")
        print("jalan "+str(jalan_total)+" kali")
        print("istirahat "+str(istrahat_total)+" kali")
        print("memalak "+str(berburu_total)+" kali")
        print("mengecek status "+str(status_total)+" kali")

        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        if pilihan == "n":
            start()

    if food <= 0:
        print("di game kamu ")
        print("selamat baru sampai di malang ")
        print("jalan "+str(jalan_total)+" kali")
        print("istirahat "+str(istrahat_total)+" kali")
        print("memalak "+str(berburu_total)+" kali")
        print("mengecek status "+str(status_total)+" kali")

        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        if pilihan == "n":
            start()

    if health <= 0:
        print("game over darah kamu habis")

        print("di game kamu")
        print("jalan "+str(jalan_total)+" kali")
        print("istirahat "+str(istrahat_total)+" kali")
        print("memalak "+str(berburu_total)+" kali")
        print("mengecek status "+str(status_total)+" kali")

        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        if pilihan == "n":
            start()

    if bulan >= 13:
        print("game over darah kamu habis")

        print("selamat baru sampai di malang")
        print("jalan "+str(jalan_total)+" kali")
        print("istirahat "+str(istrahat_total)+" kali")
        print("memalak "+str(berburu_total)+" kali")
        print("mengecek status "+str(status_total)+" kali")

        pilihan = input("apakah anda mau main (Y,N) : ")
        if pilihan == "y":
            start()
        if pilihan == "n":
            start()


def start():
    os.system("cls")
    print("selamat datang")
    return tplayer()

start()
