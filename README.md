
# Penghitung Kalori Harian

Aplikasi desktop sederhana untuk menghitung kebutuhan kalori harian berdasarkan data usia, berat badan, tinggi badan, jenis kelamin, dan tingkat aktivitas fisik pengguna.

---

## Deskripsi

Aplikasi ini menggunakan rumus **Harris-Benedict revisi** (berdasarkan sumber dari [Hello Sehat](https://hellosehat.com/nutrisi/cara-menghitung-bmr/)) untuk menghitung **BMR (Basal Metabolic Rate)**, lalu mengalikan dengan faktor aktivitas fisik untuk mendapatkan kebutuhan kalori harian.

---

## Fitur

- Input umur, berat badan (kg), tinggi badan (cm)
- Pilihan jenis kelamin (Pria/Wanita)
- Pilihan tingkat aktivitas (Tidak Aktif, Jarang Aktif, Sering Aktif)
- Hitung dan tampilkan kebutuhan kalori harian secara cepat dan mudah

---


## Rumus yang Digunakan

- Untuk **Pria**:  
  ```
  BMR = 66.5 + (13.7 × berat kg) + (5 × tinggi cm) - (6.8 × umur)
  ```
- Untuk **Wanita**:  
  ```
  BMR = 655 + (9.6 × berat kg) + (1.8 × tinggi cm) - (4.7 × umur)
  ```

- Faktor aktivitas:  
  - Tidak Aktif → kalikan 1.2  
  - Jarang Aktif → kalikan 1.3  
  - Sering Aktif → kalikan 1.4  



