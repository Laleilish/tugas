#Nama: Febriansyah Nugraha
#NIM: 2408163
#Kelas: RPL-1C


x = int(input("Masukan Jumlah Barang:"))
Harga=0
if (x>0):
    if (x<100):
        Harga = 5000
    elif (x>=100 and x<=150):
        Harga = 4000
    elif (x>150):
        Harga = 2500
else:
    print("Jumlah barang minimal 1, TIDAK BOLEH MINUS!!!")

total_harga= x*Harga
print ("Total Harga Barang", total_harga)