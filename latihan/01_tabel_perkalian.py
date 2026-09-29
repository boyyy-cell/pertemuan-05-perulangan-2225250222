# Program Tabel Perkalian
# Input: satu bilangan bulat
# Proses: melakukan perulangan dari 1 sampai 10
# Output: tabel perkalian bilangan yang dimasukkan

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")