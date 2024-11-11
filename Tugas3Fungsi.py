# Nama: Febriansyah Nugraha
# NIM: 2408163
# Kelas: 1C

def menghitung_selisih_waktu (waktu_mulai, waktu_selesai):
    mulai_jam, mulai_menit, mulai_detik = waktu_mulai
    selesai_jam, selesai_menit, selesai_detik = waktu_selesai

    #Konversi ke detik untuk menghindari minus
    mulai_dalam_detik = mulai_jam * 3600 + mulai_menit * 60 + mulai_detik
    selesai_dalam_detik = selesai_jam * 3600 + selesai_menit * 60 + selesai_detik
    selisih_waktu_detik = selesai_dalam_detik - mulai_dalam_detik
    
    #Konversi kembali ke jam, menit, detik
    jam = selisih_waktu_detik // 3600
    menit = (selisih_waktu_detik % 3600) // 60
    detik = selisih_waktu_detik % 60
    return jam, menit, detik

# Inputan waktu dari user
mulai_jam = int(input("Masukan jam mulai: "))
mulai_menit = int(input("Masukan menit mulai: "))
mulai_detik = int(input ("Masukan detik mulai: "))
selesai_jam = int(input("Masukan jam selesai: "))
selesai_menit = int(input("Masukan menir selesai: "))
selesai_detik = int (input("Masukan detik selesai: "))

# Selisih Waktu
waktu_mulai = (mulai_jam, mulai_menit, mulai_detik)
waktu_selesai = (selesai_jam, selesai_menit, selesai_detik)
jam, menit, detik = menghitung_selisih_waktu(waktu_mulai, waktu_selesai)

print (f"Selisih waktunya adalah: {jam} jam {menit} menit {detik} detik")
