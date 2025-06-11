# Tugas Pemrograman A

Repositori ini berisi source code dan laporan untuk menyelesaikan soal Tugas Pemrograman A dari mata kuliah Pemrograman.

## Deskripsi 
Data yang digunakan merupakan informasi populasi dan persentase pengguna internet di Indonesia dari tahun 1960 hingga 2023. Terdapat data yang hilang di tahun 2005, 2006, 2015, dan 2016. Tugas ini menyelesaikan masalah tersebut dengan pendekatan interpolasi dan regresi.

## Fitur
- Interpolasi data hilang (tahun 2005, 2006, 2015, 2016) menggunakan metode kubik.
- Regresi polinomial orde 3 untuk memodelkan:
  - Pertumbuhan populasi
  - Pertumbuhan persentase pengguna internet
- Prediksi populasi tahun 2030
- Prediksi jumlah pengguna internet tahun 2035
- Visualisasi grafik tren
- Bonus: Implementasi interpolasi dalam bahasa C

## Struktur Direktori
```
├── main.py                  # Implementasi analisis dan visualisasi dengan Python
├── main.c                   # Bonus: Implementasi interpolasi Lagrange dalam bahasa C
├── Data Tugas Pemrograman A.csv  # Dataset
├── grafik_regresi.png       # Hasil visualisasi grafik
├── TugasPemrogramanA_MAvicennaRaffaizA_2206062844  # Laporan
└── README.md                # File ini
```

## Contoh Hasil Interpolasi
| Tahun | Estimasi Populasi | Estimasi % Pengguna Internet |
|-------|-------------------|-------------------------------|
| 2005  | 230.894.123       | 2.86%                         |
| 2006  | 233.957.189       | 3.72%                         |
| 2015  | 261.804.545       | 20.96%                        |
| 2016  | 264.632.392       | 26.02%                        |

## Cara Menjalankan (Python)
1. Pastikan Python 3 sudah terinstall
2. Install library yang dibutuhkan:
```bash
pip install numpy pandas matplotlib scipy
```
3. Jalankan:
```bash
python main.py
```

4. Alternatif: Copy-paste semua kode python ke dalam notebook di colab, lalu tambahkan file dataset.

