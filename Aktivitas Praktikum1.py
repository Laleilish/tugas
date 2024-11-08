# Nama: Febriansyah Nugraha
# NIM : 2408163
# Kelas: RPL-1C


a = float(input("Masukan nilai jari-jarinya: "))
b = float(input("Masukan Tinggi tabung: "))

def volumetabung(a, b):
    return 3.14 * a**2 * b

volume = volumetabung(a, b)
print("Volume tabung adalah: ", volume) 