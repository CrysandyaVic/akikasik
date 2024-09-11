
# Implementasi Checklist Django Project

## Membuat Proyek Django

1. Membuat direktori sesuai dengan nama proyek: **akikasik**; ini adalah proyek e-commerce yang menjual batu akik.
2. Pada direktori tersebut, membuat **virtual environment** dengan perintah:
   ```bash
   python -m venv env
   env\Scriptsctivate
   ```
3. Membuat file `requirement.txt` untuk menyimpan dependencies yang diperlukan dan menginstal dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```
4. Membuat proyek Django dengan perintah:
   ```bash
   django-admin startproject akikasik .
   ```
5. Menambahkan konfigurasi `ALLOWED_HOST` pada file `settings.py` agar jaringan lokal dapat mengakses aplikasi:
   ```python
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
   ```
6. Menjalankan server untuk mengecek apakah proyek Django dapat berjalan:
   ```bash
   python manage.py runserver
   ```

## Membuat Aplikasi "main" dan Routing

1. Pada direktori utama (akikasik), jalankan perintah untuk membuat aplikasi:
   ```bash
   python manage.py startapp main
   ```
2. Mendaftarkan aplikasi `main` ke dalam proyek dengan menambahkan `main` ke dalam daftar `INSTALLED_APPS` di `settings.py`.

## Membuat Template dan Model

1. Membuat file `main.html` di direktori `templates/main` untuk menampilkan produk dengan atribut **nama**, **harga**, dan **deskripsi**.
2. Pada `models.py` di dalam aplikasi `main`, buat class `Produk` dengan atribut:
   - `name`: `CharField`
   - `price`: `IntegerField`
   - `description`: `TextField`
   - `image`: `CharField`

## Membuat Fungsi Views

1. Pada file `views.py`, buat fungsi `show_main` untuk menampilkan produk dengan nama, harga, dan deskripsi di `main.html`.

## Routing URL

1. Pada `urls.py` di direktori `main`, tambahkan:
   ```python
   urlpatterns = [
       path('', show_main, name='show_main'),
   ]
   ```
2. Pada `urls.py` di direktori proyek `akikasik`, impor fungsi `include` dan buat path ke aplikasi `main`.

## Deploy Proyek

1. Menambahkan proyek ke repositori GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. Deploy proyek di **PWS**.

---
## Bagan request client ke web aplikasi berbasis Django
[Django Bagan](Bagan request client ke web aplikasi berbasis Django)
## Kegunaan Git

**Git** adalah sistem kontrol versi yang dikembangkan oleh Linus Torvalds. Beberapa kegunaannya adalah:

- **Pelacakan Perubahan**: Merekam setiap perubahan pada kode, memungkinkan rollback jika ada kesalahan.
- **Kolaborasi**: Memfasilitasi kerja tim dengan salinan lokal yang independen.
- **Branching dan Merging**: Pengembangan fitur secara terpisah tanpa mengganggu kode utama.
- **Resolusi Konflik**: Menyelesaikan konflik saat banyak pengembang mengubah file yang sama.

---

## Mengapa Django Dipilih sebagai Framework untuk Pembelajaran?

1. **Bahasa Python**: Karena mahasiswa sudah mempelajari Python sejak awal, penggunaan Django yang berbasis Python menjadi lebih mudah dipahami.
2. **Banyak Referensi**: Django memiliki komunitas yang aktif dan dokumentasi lengkap, memudahkan proses pembelajaran.
3. **Framework yang Terpercaya**: Digunakan oleh banyak perusahaan besar seperti Instagram, Pinterest, dan Mozilla.
4. **Fleksibilitas dan Skalabilitas**: Django dapat digunakan untuk proyek kecil hingga besar dan memiliki berbagai modul siap pakai.

---

## Mengapa Model pada Django Disebut ORM?

**ORM (Object-Relational Mapping)** adalah teknik pemrograman yang memungkinkan pengelolaan database dengan konsep objek dalam bahasa pemrograman. Pada Django, model berfungsi sebagai ORM, memetakan objek Python ke tabel-tabel dalam database relasional. Ini memungkinkan pengembang berinteraksi dengan database tanpa perlu menulis query SQL langsung.
