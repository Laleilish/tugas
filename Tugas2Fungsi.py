# Nama: Febriansyah Nugraha
# NIM: 2408163
# Kelas: RPL-1C

def login ():
    password_sistem = "Latihan"
    max = 3 

    print("Selamat Datang!, Login dengan 3 kesempatan")
    print("Username: Daspro2023") # Di print langsung karena sistem tidak peduli dengan username

    # Loop untuk mengizinkan pengguna memasukkan password
    for kesempatan in range(1, max + 1):
        password_input = input("Masukkan password: ")

        if password_input == password_sistem: # Jika password yang dimasukkan benar
            print("Login berhasil! Selamat datang!")
            break
        else:
            sisa = max - kesempatan # Menghitung sisa kesempatan
            if sisa > 0:
                print(f"Password salah! Anda memiliki {sisa} kesempatan lagi")
            else:
                print("Anda telah gagal login sebanyak 3 kali. Akses ditolak.")

login () # Memanggil fungsi login
