
# TUGAS 2

## Deployment

Tautan aplikasi PWS: [https://pbp.cs.ui.ac.id/web/project/crysandya.vic/akikasik2]

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
![Django Bagan](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/Diagram.jpg)
## Kegunaan Git

**Git** adalah sistem kontrol versi yang dikembangkan oleh Linus Torvalds. Beberapa kegunaannya adalah:

- **Pelacakan Perubahan**: Git memungkinkan pengembang untuk melacak setiap perubahan yang dilakukan pada kode. Ini memudahkan pengembang untuk melihat riwayat perubahan dan mengembalikan kode ke versi sebelumnya jika terjadi kesalahan.
- **Kolaborasi**: Git memfasilitasi kerja sama pada sebuah tim dengan menyediakan salinan lokal proyek untuk setiap pengembang. Mereka dapat mengerjakan proyek secara independen dan kemudian menggabungkan perubahan ke dalam versi utama.
- **Branching dan Merging**: Fitur branching memungkinkan pengembang untuk membuat cabang terpisah guna bekerja pada fitur atau perbaikan tertentu tanpa mengganggu kode utama. Setelah selesai, cabang tersebut dapat digabungkan kembali (merging) ke dalam versi utama.
- **Resolusi Konflik**: Saat beberapa pengembang mengedit file yang sama, Git menyediakan mekanisme untuk mendeteksi dan menyelesaikan konflik perubahan tersebut, memastikan integritas proyek tetap terjaga.

---

## Mengapa Django Dipilih sebagai Framework untuk Pembelajaran?

1. **Bahasa Python**: Framework Django menggunakan bahasa pemrograman python. Bahasa pemrograman python sudah dipelajari oleh mahasiswa fasilkom sejak DDP 1 ketika semester 1, sehingga kebanyakan dari kita sudah memahami cara penulisan program dengan bahasa tersebut
2. **Banyak Referensi**: Django memiliki komunitas yang sangat aktif dan profesional. Dokumentasi resmi Django adalah sumber daya yang sangat berharga untuk belajar, dengan tutorial, panduan referensi, dan topik lanjutan yang membantu memahami cara kerja Django.
3. **Framework yang Terpercaya**: Django digunakan oleh banyak perusahaan terkemuka seperti Instagram, National Geographic, Spotify, Mozilla, dan Pinterest. Penggunaan yang luas ini menunjukkan kepercayaan besar pada framework ini. Django telah digunakan dalam berbagai kasus penggunaan, mulai dari aplikasi web kecil hingga aplikasi besar yang membutuhkan skalabilitas tinggi.
4. **Fleksibilitas dan Skalabilitas**: Django dikenal karena fleksibilitas dan skalabilitasnya yang tinggi, membuatnya cocok untuk proyek-proyek web berskala besar. Selain itu, Django menyediakan modul-modul yang lengkap untuk berbagai kebutuhan, seperti modul untuk menghandle email, modul untuk menghandle file, dan lain-lain. Bahkan, Django memiliki banyak ekstensi yang dapat diinstal untuk menambahkan fitur-fitur baru ke dalam aplikasi, sehingga memungkinkan pengembang untuk menyesuaikan aplikasi dengan kebutuhan spesifik mereka.
---

## Mengapa Model pada Django Disebut ORM?

ORM (Object-Relational Mapping) adalah teknik dalam pemrograman yang memungkinkan pengembang untuk mengelola dan berinteraksi dengan database relasional menggunakan konsep objek dalam bahasa pemrograman. ORM berfungsi sebagai jembatan antara database relasional (seperti MySQL, PostgreSQL, atau SQLite) dan kode program yang ditulis menggunakan bahasa berorientasi objek. Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena berfungsi sebagai alat yang memetakan objek dalam kode Python ke tabel-tabel di database relasional. Django ORM memungkinkan pengembang bekerja dengan data dari database menggunakan konsep objek dalam bahasa Python, tanpa harus menulis query SQL secara langsung. 
