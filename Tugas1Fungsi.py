# Nama: Febriansyah Nugraha
# NIM : 2408163
# Kelas: RPL-1C

def fibonacci (n):
    a, b = 0, 1
    urutan_fibonacci = []

    for i in range (n):
        urutan_fibonacci.append (a)
        a, b = b, a + b
    return urutan_fibonacci

n = int(input("Masukan berapa deret Fibonaccinya: "))
print("Deret Fibonacci: ", fibonacci(n))
