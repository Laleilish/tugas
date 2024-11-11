# Nama: Febriansyah Nugraha
# NIM : 2408163
# Kelas: RPL-1C

#menghitung rata- rata
def nilai_ratarata(*angka):
    if len(angka) == 0:
        return 0
    total = sum(angka)
    rata_rata = total / len(angka)
    return (f"Nilai rata-ratanya adalah: {rata_rata}")

print (nilai_ratarata(2, 3, 5, 10))
print (nilai_ratarata(5, 10))