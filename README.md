# Pertemuan 05 Perulangan Python

**Nama:** Farid Syahputra
**NIM:** 2225250222
**Kelas:** 3F
**Mata Kuliah:** Algoritma dan Pemrograman
**Program Studi:** Pendidikan Matematika
**Fakultas:** FKIP
**Universitas:** Universitas Sultan Ageng Tirtayasa

---

## Tujuan

Mempelajari dan menerapkan perulangan `for` dan `while` dalam Python untuk menyelesaikan masalah iteratif.

Pada pertemuan ini dipelajari konsep iterasi, kondisi berhenti, perubahan nilai variabel, akumulasi, pencacahan, validasi input berulang, serta penggunaan seleksi `if` di dalam perulangan.

---

## Struktur Folder

```text
pertemuan-05-perulangan-2225250222/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_tabel_perkalian.py
│   ├── 02_jumlah_bilangan.py
│   ├── 03_validasi_input.py
│   └── 04_hitung_genap.py
│
└── kuis/
    └── kuis2_deret_aritmetika.py
```

---

## Materi yang Dipelajari

Materi Pertemuan 05 meliputi:

1. Konsep iterasi dan tracing.
2. Perulangan `for`.
3. Fungsi `range()`.
4. Perulangan `while`.
5. Kondisi berhenti.
6. Validasi input berulang.
7. Seleksi `if` di dalam perulangan.
8. Akumulasi dan pencacahan.
9. Debugging perulangan di VS Code.
10. Penggunaan Git dan GitHub.

---

# Latihan

## 1. Tabel Perkalian

File:

```text
latihan/01_tabel_perkalian.py
```

Program menerima satu bilangan bulat dan menampilkan tabel perkalian dari 1 sampai 10 menggunakan perulangan `for`.

### Cara Menjalankan

```bash
python latihan/01_tabel_perkalian.py
```

### Test Case

**Input:**

```text
4
```

**Output:**

```text
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```

Test case kedua menggunakan:

```text
-3
```

Program harus tetap menghasilkan 10 baris keluaran.

---

## 2. Jumlah Bilangan 1 sampai n

File:

```text
latihan/02_jumlah_bilangan.py
```

Program menerima bilangan bulat positif `n`, kemudian menghitung jumlah:

```text
1 + 2 + 3 + ... + n
```

Perulangan menggunakan `for` dan variabel `total` sebagai akumulator.

### Cara Menjalankan

```bash
python latihan/02_jumlah_bilangan.py
```

### Test Case

| Input n | Hasil |
| ------: | ----: |
|       1 |     1 |
|       5 |    15 |
|      10 |    55 |

---

## 3. Validasi Input

File:

```text
latihan/03_validasi_input.py
```

Program meminta pengguna memasukkan nilai ujian dari 0 sampai 100.

Jika nilai berada di luar rentang tersebut, program akan meminta input kembali menggunakan perulangan `while`.

### Cara Menjalankan

```bash
python latihan/03_validasi_input.py
```

### Test Case

Input:

```text
120
-5
75
```

Output:

```text
Nilai tidak valid.
Nilai tidak valid.
Nilai diterima: 75.0
```

Program berhenti setelah pengguna memasukkan nilai yang valid.

---

## 4. Menghitung Bilangan Genap

File:

```text
latihan/04_hitung_genap.py
```

Program menerima bilangan positif `n` dan menghitung banyak bilangan genap dari 1 sampai `n`.

Program menggunakan kombinasi perulangan `for` dan seleksi `if`.

### Cara Menjalankan

```bash
python latihan/04_hitung_genap.py
```

### Test Case

|  n | Hasil |
| -: | ----: |
|  1 |     0 |
|  2 |     1 |
|  5 |     2 |
| 10 |     5 |

---

# Kuis 2 - Deret Aritmetika

File:

```text
kuis/kuis2_deret_aritmetika.py
```

Program menerima:

* `a` = suku pertama
* `d` = beda
* `n` = banyak suku

Program menggunakan `while` untuk melakukan validasi nilai `n` dan menggunakan `for` untuk menghasilkan deret sebanyak `n` suku.

Setiap suku dihitung menggunakan:

```text
suku = a + i * d
```

Kemudian setiap suku dijumlahkan menggunakan variabel `total`.

---

## Algoritma Kuis 2

1. Menampilkan judul program.
2. Membaca suku pertama `a`.
3. Membaca beda `d`.
4. Membaca banyak suku `n`.
5. Memeriksa apakah `n` lebih kecil atau sama dengan 0.
6. Jika `n <= 0`, meminta input `n` kembali menggunakan `while`.
7. Menginisialisasi `total = 0`.
8. Melakukan perulangan `for` sebanyak `n` kali.
9. Menghitung nilai suku.
10. Menambahkan nilai suku ke `total`.
11. Menampilkan nomor dan nilai setiap suku.
12. Menampilkan jumlah seluruh suku setelah perulangan selesai.

---

## Cara Menjalankan Kuis

```bash
python kuis/kuis2_deret_aritmetika.py
```

---

## Test Case Kuis 2

| No |   a |   d |  n | Suku            | Jumlah | Status   |
| -- | --: | --: | -: | --------------- | -----: | -------- |
| 1  |   2 |   3 |  5 | 2, 5, 8, 11, 14 |  40.00 | Berhasil |
| 2  |  10 |  -2 |  4 | 10, 8, 6, 4     |  28.00 | Berhasil |
| 3  | 1.5 | 0.5 |  3 | 1.5, 2.0, 2.5   |   6.00 | Berhasil |

---

## Contoh Tracing Kuis 2

Digunakan:

```text
a = 2
d = 3
n = 5
```

| Iterasi |  i | Suku | Total Sebelum | Total Sesudah |
| ------: | -: | ---: | ------------: | ------------: |
|       1 |  0 |    2 |             0 |             2 |
|       2 |  1 |    5 |             2 |             7 |
|       3 |  2 |    8 |             7 |            15 |
|       4 |  3 |   11 |            15 |            26 |
|       5 |  4 |   14 |            26 |            40 |

Jumlah akhir:

```text
40.00
```

---

# Hasil Pengujian

Seluruh program telah diuji menggunakan beberapa test case.

| Program          | Pengujian   | Hasil    |
| ---------------- | ----------- | -------- |
| Tabel Perkalian  | n = 4       | Berhasil |
| Tabel Perkalian  | n = -3      | Berhasil |
| Jumlah Bilangan  | n = 5       | Berhasil |
| Jumlah Bilangan  | n = 10      | Berhasil |
| Validasi Input   | 120, -5, 75 | Berhasil |
| Hitung Genap     | n = 5       | Berhasil |
| Hitung Genap     | n = 10      | Berhasil |
| Deret Aritmetika | 2, 3, 5     | Berhasil |
| Deret Aritmetika | 10, -2, 4   | Berhasil |
| Deret Aritmetika | 1.5, 0.5, 3 | Berhasil |

---

# Refleksi

Pada Pertemuan 05 saya mempelajari penggunaan perulangan `for` dan `while` dalam Python.

`for` digunakan ketika jumlah iterasi sudah diketahui atau ketika program perlu mengunjungi suatu urutan nilai. Sedangkan `while` digunakan ketika proses perulangan dikendalikan oleh suatu kondisi.

Kesalahan yang perlu diperhatikan dalam perulangan adalah batas `range`, kondisi berhenti pada `while`, pembaruan variabel kontrol, dan posisi akumulator.

Pada Kuis 2, `while` digunakan untuk melakukan validasi input `n`, sedangkan `for` digunakan untuk menghasilkan deret karena jumlah iterasinya sudah diketahui dari nilai `n`.

Variabel `total` harus diinisialisasi sebelum perulangan agar hasil penjumlahan dapat terus diperbarui pada setiap iterasi.

---

# Kesimpulan

Perulangan merupakan struktur kontrol yang digunakan untuk menjalankan suatu proses secara berulang.

Perulangan `for` sesuai digunakan ketika jumlah iterasi atau urutan nilai sudah diketahui, sedangkan `while` sesuai digunakan ketika perulangan bergantung pada kondisi tertentu.

Penggunaan tracing membantu mengetahui perubahan nilai variabel pada setiap iterasi dan membantu menemukan kesalahan pada batas perulangan, kondisi berhenti, maupun akumulasi.

---

# Git dan GitHub

Repository ini digunakan untuk mengumpulkan hasil latihan dan Kuis 2 Pertemuan 05.

Beberapa commit yang digunakan:

```bash
git add .
git commit -m "feat: menambahkan latihan perulangan pertemuan 05"

git add latihan
git commit -m "feat: menyelesaikan latihan for dan while"

git add kuis/kuis2_deret_aritmetika.py
git commit -m "feat: menyelesaikan kuis 2 deret aritmetika"

git add README.md
git commit -m "docs: menambahkan hasil uji dan refleksi"
```

Perubahan kemudian dikirim ke GitHub menggunakan:

```bash
git push
```

---

# Referensi

* Materi Pertemuan 05 Algoritma dan Pemrograman - Perulangan `for` dan `while` dalam Python.
* Python Documentation.
* Visual Studio Code Documentation.
* GitHub Documentation.
