#####################################
#Nama  : Raden Hamizan Rizky Kusuma
#NIM   : 2403657
#Kelas : 1C
#####################################

#menghitung nilai rata rata

def totalangka(*angka):
    if len(angka) == 0:
        return 0
    total = sum(angka)
    ratatara = total / len(angka)
    return(f"nilai rata ratanya adalah {ratatara}")


print(totalangka(2, 3, 5, 10))
print(totalangka(5, 10))