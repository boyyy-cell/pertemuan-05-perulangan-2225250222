# Kuis 2 - Deret Aritmetika
# Input:
# a = suku pertama
# d = beda
# n = banyak suku
#
# Proses:
# 1. Validasi n menggunakan while
# 2. Menghasilkan suku menggunakan for
# 3. Mengakumulasikan jumlah seluruh suku
#
# Output:
# Menampilkan setiap suku dan jumlah akhir

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")