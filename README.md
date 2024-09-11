Implementasi Checklist : 
Membuat proyek Django
Membuat direktori sesuai dengan nama proyek ini ; akikasik; saya membuat e-commerce yang menjual batu akik.
Pada direktori tersebut saya membuat virtual enviroment dengan menulis beberapa perintah pada command prompt : 
python -m venv env
env\Scripts\activate
Membuat “requirement.txt” untuk menampung dependencies-dependencies yang diperlukan pada proyek ini. Lalu install setiap dependencies dengan perintah : 
pip install -r requirements.txt
Membuat proyek Django dengan perintah : django-admin startproject akikasik .
Agar jaringan saya (lokal) dapet mengakses aplikasi web perlu melakukan konfigurasi dengan menambahkan daftar host pada variabel ALLOWED_HOST pada settings.py. Yang ditambahkan adalah ["localhost", "127.0.0.1"]
Run server untuk mengecek apakah proyek Django dapat berjalan.
Membuat aplikasi “main” dan routing
Pada direktori paling luar (akikasik) jalankan perintah : python manage.py startapp main. Setelah itu akan muncul direktori main yang berisi struktur aplikasi di dalam direktori utama (akikasik).
Mendaftarkan aplikasi main kedalam proyek dengan menambahkan elemen ‘main’ pada list INSTALLED_APPS yang berada di settings.py