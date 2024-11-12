#####################################
#Nama  : Raden Hamizan Rizky Kusuma
#NIM   : 2403657
#Kelas : 1C
#####################################

def check(password):
    return password == "latihan"

def berhasil():
    print("Selamat datang di aplikasi Dasar Pemrograman")

def gagal(kesempatan):
    print(f"Login salah! Kesempatan anda {kesempatan} kali lagi")

def ditolak():
    print("Anda tidak diperkenankan mengakses aplikasi ini")

def login():
    print("Silakan Login")
    print("Login dengan 3 Kesempatan")
    
    for kesempatan in range(3, 0, -1):
        username = input("Username: ")
        password = input("Password: ")
        
        if check(password):
            berhasil()
            break
        else:
            gagal(kesempatan - 1)
    else:
        ditolak()

login()