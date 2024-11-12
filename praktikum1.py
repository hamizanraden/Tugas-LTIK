#####################################
#Nama  : Raden Hamizan Rizky Kusuma
#NIM   : 2403657
#Kelas : 1C
#####################################

def volume_tabung(ruas, tinggi):
    volume = 3.14 * (ruas**2) * tinggi
    return volume

input_ruas = int(input("Masukkan ruas:  "))
input_tinggi = int(input("Masukkan tinggi:  "))
hasil = volume_tabung (input_ruas, input_tinggi)
print(f"Volume tabung adalah: {hasil:.2f}")