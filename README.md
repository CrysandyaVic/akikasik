
# TUGAS 2

## Deployment

Tautan aplikasi PWS: [https://pbp.cs.ui.ac.id/web/project/crysandya.vic/akikasik]

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


# TUGAS 3

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

1. Data delivery memungkinkan berbagai bagian dari platform untuk saling bertukar informasi. Ini memastikan bahwa data yang diperlukan bisa dikirim dan diterima dengan benar di seluruh sistem.
2. Sistem yang efisien dalam mengelola data delivery akan memiliki performa yang lebih baik. Pengiriman data yang cepat membuat aplikasi lebih responsif dan meningkatkan pengalaman pengguna.
3. Data delivery juga melibatkan perlindungan data. Ini memastikan bahwa data yang dikirim aman dari akses tidak sah melalui teknik seperti enkripsi dan autentikasi.
4. Data delivery memudahkan berbagai sistem untuk berinteraksi dan bertukar data dengan cara yang standar, membuat integrasi sistem lebih mudah.


## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Setelah membuat tugas 3 ini saya dapat melihat bentuk dari JSON dan XML secara langsung. Kedua format itu memiliki ciri khasnya masing-masing. Struktur JSON menggunakan pasangan kunci-nilai (key-value pairs) yang disusun dalam objek. Objek JSON dikelilingi oleh kurung kurawal {} dan di dalamnya terdapat pasangan kunci-nilai yang dipisahkan oleh koma. Sedangkan XML menggunakan tag pembuka dan penutup untuk membungkus data. Tag-tag ini membentuk struktur hierarki yang disebut elemen. Dari kedua format tersebut, saya lebih mudah membaca isi dari JSON. 

JSON sering dipilih sebagai format untuk pemrosesan data karena banyak kelebihannya. Dibandingkan dengan XML, JSON lebih padat dan ringkas, sehingga proses parsing dan pembuatannya lebih cepat. Ini membantu mengurangi ukuran data dan penggunaan bandwidth dalam transfer, sekaligus meningkatkan efisiensi serta kinerja pemrosesan data. Di samping itu, JSON lebih mudah dibaca dan ditulis daripada XML, yang mempermudah dalam hal keterbacaan dan pemeliharaan kode. JSON juga memiliki dukungan untuk tipe data asli seperti angka, boolean, dan null, yang menyederhanakan representasi serta validasi data. Selain itu, kompatibilitas JSON dengan JavaScript dan berbagai teknologi web lainnya menjadikannya lebih mudah digunakan dalam pengembangan aplikasi web dan API.


## Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() digunakan untuk melakukan validasi pada setiap field form dan didefinisikan dalam kelas Form Django. Method ini akan mengembalikan nilai True jika data valid, serta menyimpan semua data ke dalam atribut cleaned_data.

**Method ini dibutuhkan untuk:**

1. Memastikan integritas data: Form sering digunakan untuk menerima input dari pengguna, dan method ini memastikan bahwa data yang dimasukkan sesuai dengan aturan yang ditentukan, mencegah kesalahan atau eksploitasi yang dapat terjadi karena data yang tidak valid.
2. Memudahkan penanganan error: Dengan adanya method ini, developer bisa dengan mudah mendeteksi dan menangani kesalahan, menampilkan pesan error yang relevan kepada pengguna, serta memastikan hanya data yang valid yang diproses lebih lanjut.



## Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

**Cross-Site Request Forgery (CSRF)** adalah jenis serangan yang memaksa pengguna untuk melakukan tindakan yang tidak diinginkan pada aplikasi web tempat mereka terautentikasi. Penyerang dapat memanfaatkan teknik rekayasa sosial, seperti mengirimkan tautan melalui email atau chat, untuk menipu pengguna agar melakukan aksi yang diinginkan oleh penyerang.

Django menyediakan fitur untuk mencegah serangan semacam ini. Saat pengguna terautentikasi dan menjelajahi situs, Django menghasilkan csrf_token unik untuk setiap sesi. Token ini disertakan dalam form atau permintaan yang dikirim oleh pengguna dan diperiksa oleh server untuk memastikan bahwa permintaan tersebut berasal dari pengguna yang sah, bukan dari sumber lain.

Jika kita tidak menambahkan csrf_token, aplikasi web menjadi rentan terhadap serangan CSRF. Memungkinkan penyerang untuk mengirimkan permintaan jahat terhadap kredensial pengguna yang sah, yang dapat menyebabkan:

1. Kerentanan terhadap Serangan CSRF: Tanpa csrf_token, form dapat digunakan oleh penyerang untuk mengirimkan permintaan jahat.

2. Tindakan Tidak Sah: Penyerang dapat melakukan tindakan berbahaya seperti mengubah data atau melakukan transaksi yang merugikan.

**Penyerang dapat memanfaatkan hal ini dengan:**

1. Membuat Form Berbahaya: Menghasilkan form di situs web mereka atau melalui tautan yang dikirimkan kepada pengguna.

2. Pengiriman Permintaan Berbahaya: Saat pengguna yang terautentikasi mengisi form tersebut, permintaan jahat dikirim ke aplikasi web target.

3. Eksekusi Aksi Tidak Diinginkan: Melakukan tindakan berbahaya atas nama pengguna, seperti mengubah pengaturan atau melakukan transaksi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

**Membuat kerangka views**

1. Membuat direktori templates pada root folder
2. Pada direktori tersebut buat base.html yang berisi template dasar untuk halaman web yang lain

**Mengubah Primary Key dari int - UUID**

1. Pada file models.py pada main lakukan import dan menambah atribut dari class Product 
 ```bash
import uuid
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   ```

2. Melakukan migrasi model

**Membuat form input**

1. Pada file forms.py pada main menambahkan import baru dan juga membuat class untuk form

```from django.forms import ModelForm
from main.models import Products

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["nama", "harga", "deskripsi"]
   ```

2. Pada file views.py pada main menambahkan import redirect dan menambah fungsi baru yang dapat membuat form dan menambah data

```def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)
```

3. Pada fungsi show_main pada file views.py tambahkan variabel baru dan elemen baru pada context

  ```return re
product_entries = Products.objects.all()
'product_form': product_entries,
```

4. Membuat file html baru bernama create_product_entry.html pada subdirektori templates yang berada pada main

```{% extends 'base.html' %}
{% block content %}
<h1>Add New Product Entry</h1>

<form method="POST">
 {% csrf_token %}
 <table>
   {{ form.as_table }}
   <tr>
     <td></td>
     <td>
       <input type="submit" value="Add Product Entry" />
     </td>
   </tr>
 </table>
</form>

{% endblock %}
```

5. Pada main.html tambahkan beberapa baris kode di dalam {% block content %}

```t %} 
{% if not product_form %}
<p>Belum ada data batu pada akikasik.</p>
{% else %}
<table>
  <tr>
    <th>Nama Batu</th>
    <th>Harga</th>
    <th>Deskripsi</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini 
  {% endcomment %} 
  {% for product_entry in product_form %}
  <tr>
    <td>{{ product_entry.nama }}</td>
    <td>{{ product_entry.harga }}</td>
    <td>{{ product_entry.deskripsi }}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_product_entry' %}">
  <button>Add New Product Entry</button>
</a>

{% endblock content %}
```

**Membuat fungsi fungsi untuk mengembalikan data**

1. Pada file views.py membuat fungsi yang akan mengambalikan data-data dalam bentuk XML dan JSON

```def show_xml(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```


**Routing URLs**

1. Pada urls.py di main melakukan import

```
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
```

2. Melakukan penambahan elemen pada urlpatterns

```
path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

## POSTMEN
![Django Bagan](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/postman1.png)

![Django Bagan](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/postman2.png)

![Django Bagan](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/postman3.png)

![Django Bagan](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/postman4.png)



# TUGAS 4

## Apa perbedaan antara HttpResponseRedirect() dan redirect()
Kedua fungsi ini memiliki peran yang sama yaitu digunakan di Django untuk mengarahkan (redirect) pengguna dari satu URL ke URL lainnya. Keduanya melakukan redirect, tetapi memiliki perbedaan : 

* **HttpResponseRedirect()** : memerlukan URL string sebagai argumen, yang menentukan ke mana pengguna akan diarahkan.

* **redirect()** : dapat menerima URL string, nama dari view (dengan atau tanpa argumen), atau bahkan model object, dan akan secara otomatis mengonversinya ke URL yang sesuai. redirect mengenkapsulasi (menggabungkan) HttpResponseRedirect dan HttpResponsePermanentRedirect dengan argumen permanent=False.

Fungsi redirect() lebih fleksibel untuk digunakan karena dapat menerima banyak format, tapi tidak ada keunggulan yang signifikan jika dibandingkan dengan HttpResponseRedirect()

## Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User bertujuan agar dapat melihat produknya masing-masing tanpa tercampur dengan produk user lain. Penghubungan ini dapat dilakukan menggunakan  foreign key atau one-to-one relationship dalam model Django.

**Cara Kerja** :

* Relasi antara Products dan User dilakukan menggunakan ForeignKey. ForeignKey adalah tipe field yang memungkinkan model Product untuk merujuk pada model User.
Setiap kali sebuah produk dibuat, produk tersebut akan dikaitkan dengan satu pengguna yang memiliki produk itu.

* **User yang Login Sebagai Pemilik Produk** : Relasi ini memungkinkan kita untuk membuat produk baru yang terhubung dengan pengguna yang sedang login. Dalam praktiknya, informasi pengguna diambil dari objek ```request.user``` saat produk dibuat.
Penghapusan Terkait (Cascade)

* Dalam ```models.py```, terdapat opsi ```on_delete=models.CASCADE```. Opsi ini memastikan bahwa jika pengguna dihapus dari basis data, semua produk yang terkait dengan pengguna tersebut juga akan dihapus secara otomatis. Cara mencegah produk yang tidak memiliki pemilik ("orphaned") tertinggal di basis data.


## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Authentication**
merupakan proses verifikasi/penyocokan identitas pengguna, biasanya melalui pengisian username dan password. Proses ini memastikan bahwa pengguna yang mencoba masuk sesuai dengan akun miliknya.
* Implementasi Django: Django menyediakan modul django.contrib.auth untuk menangani proses autentikasi, termasuk fungsi seperti authenticate() dan login() yang memverifikasi kredensial pengguna.

**Authorization**
Setelah pengguna berhasil diautentikasi, authorization menentukan hak akses pengguna. Proses ini menentukan apakah pengguna yang diautentikasi memiliki izin untuk melakukan tindakan tertentu atau mengakses data tertentu.
* Implementasi Django: Django menggunakan sistem permissions dan groups untuk mengelola otorisasi. Permissions dapat diberikan kepada user atau group, dan Django akan memeriksa apakah pengguna memiliki izin yang diperlukan menggunakan metode seperti has_perm().

**Yang terjadi saat pengguna login**:
Username dan password pengguna diverifikasi menggunakan fungsi authenticate().
Jika berhasil, Django membuat sesi untuk pengguna dan menyimpan informasi identitas mereka di cookie sesi. Pengguna kemudian bisa mengakses area yang membutuhkan login dengan otorisasi yang sesuai.

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django menggunakan cookies dan sessions untuk mengingat pengguna yang telah login. Saat pengguna login ke aplikasi Django, server mengirimkan cookie ke browser pengguna. Cookie ini berisi session ID, yang merupakan kunci untuk mengidentifikasi sesi pengguna yang tersimpan di server. Informasi penting seperti status login pengguna disimpan dalam session di server, bukan di cookie itu sendiri.

Kegunaan lain dari cookie:
* **Preferensi pengguna**: Cookies dapat menyimpan pengaturan atau preferensi pengguna, seperti bahasa yang dipilih atau tema.
* **Pelacakan aktivitas**: Banyak website menggunakan cookies untuk melacak aktivitas pengguna, seperti halaman apa yang dikunjungi, barang yang dilihat, atau iklan yang diklik, untuk keperluan analitik dan personalisasi iklan.
* **Keranjang belanja**: Di e-commerce, cookies bisa digunakan untuk menyimpan informasi sementara tentang barang-barang yang dimasukkan ke dalam keranjang belanja.

Tidak semua cookies aman:
* **Third-parties** : Cookies sering digunakan oleh perusahaan pihak ketiga untuk melacak aktivitas pengguna di berbagai situs web tanpa sepengetahuan atau izin mereka. Misalnya, perusahaan iklan dapat menggunakan third-party cookies untuk membuat profil perilaku pengguna berdasarkan situs web yang mereka kunjungi, yang kemudian digunakan untuk menyajikan iklan yang ditargetkan. Hal ini dapat menimbulkan masalah privasi, terutama jika data tersebut dijual atau dibagikan tanpa persetujuan pengguna.
* **Session Hijacking** : Cookies yang tidak dilindungi dapat diambil oleh penyerang melalui jaringan yang tidak aman (misalnya, Wi-Fi publik) atau melalui serangan lain. Dengan mencuri session ID dalam cookie, penyerang dapat menyamar sebagai pengguna tersebut di situs web tanpa perlu mengetahui kata sandi.
* **Cookie Reuse** : Penyerang dapat menggunakan kembali cookie dari sesi yang sudah kadaluwarsa atau mencoba memperpanjang sesi dengan mengatur ulang cookie session. Jika cookie tidak diatur untuk kadaluwarsa atau memiliki durasi yang terlalu panjang, penyerang dapat memanfaatkannya untuk mengambil alih sesi pengguna di kemudian hari.

## Implementasi Step-by-Step
**Membuat fungsi dan form registrasi, login, logout**

1. Pada views.py yang ada pada main melakukan beberapa import dan membuat fungsi register Sebelum membuat fungsi perlu import beberapa hal terlebih dahulu 
``` from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
```
**Registrasi**
```def register(request):
   form = UserCreationForm()

   if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Your account has been successfully created!')
           return redirect('main:login')
   context = {'form':form}
   return render(request, 'register.html', context)
   ```
**Login**

Agar mencegah pengguna mengakses main sebelum login maka diperlukan sebuah dekorator. Sebelum pengaplikasian dekorator perlu melakukan import

```
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def login_user(request):
  if request.method == 'POST':
     form = AuthenticationForm(data=request.POST)

     if form.is_valid():
           user = form.get_user()
           login(request, user)
           return redirect('main:show_main')

  else:
     form = AuthenticationForm(request)
  context = {'form': form}
  return render(request, 'login.html', context)
  ```


**Logout**
```
def logout_user(request):
   logout(request)
   return redirect('main:login')
   ```
2. Membuat file html baru sebagai tampilan registrasi, login dan logout pada direktori main/templates. Register dan login memiliki htmlnya sendiri, sedangkan logout berada pada main.html

**register.html**
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
 <h1>Register</h1>

 <form method="POST">
   {% csrf_token %}
   <table>
     {{ form.as_table }}
     <tr>
       <td></td>
       <td><input type="submit" name="submit" value="Daftar" /></td>
     </tr>
   </table>
 </form>

 {% if messages %}
 <ul>
   {% for message in messages %}
   <li>{{ message }}</li>
   {% endfor %}
 </ul>
 {% endif %}
</div>

{% endblock content %}
```


**login.html**
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
 <h1>Login</h1>

 <form method="POST" action="">
   {% csrf_token %}
   <table>
     {{ form.as_table }}
     <tr>
       <td></td>
       <td><input class="btn login_btn" type="submit" value="Login" /></td>
     </tr>
   </table>
 </form>

 {% if messages %}
 <ul>
   {% for message in messages %}
   <li>{{ message }}</li>
   {% endfor %}
 </ul>
 {% endif %} Don't have an account yet?
 <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```


**logout(main.html)**
```
<a href="{% url 'main:logout' %}">
 <button>Logout</button>
</a>
```
3. Mengimpor fungsi di urls.py dan tambahkan ke dalam urlpatterns
from main.views import register, login_user, logout_user
Yang ditambah pada urlpatterns adalah:
```
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

**Menggunakan data dari cookies**
1. Pada views.py direktori main tambahkan beberapa import
```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

2. Menambahkan beberapa baris kode pada fungsi login_user di views.py
```
if form.is_valid():
   user = form.get_user()
   login(request, user)
   response = HttpResponseRedirect(reverse("main:show_main"))
   response.set_cookie('last_login', str(datetime.datetime.now()))
   return response
   ```

3. Menambahkan elemen pada dictionary context pada fungsi show_main
```
'last_login': request.COOKIES['last_login'],
```

4. Memperbarui fungsi logout_user
```
def logout_user(request):
   logout(request)
   response = HttpResponseRedirect(reverse('main:login'))
   response.delete_cookie('last_login')
   return response
```
**Menghubungkan Model dengan User**

1. Melakukan impor pada models.py
```
from django.contrib.auth.models import User
```
2. Update class Product
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
3. Update fungsi create_product_entry dan show_main pada views.py

```
def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = request.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_mood_entry.html", context)
```

```
    def show_main(request):
    mood_entries = MoodEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
```
4. Lakukan migrasi model
5. Pada settings.py lakukan import dan update variable DEBUG
```
import os

PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```


## SS Account dan dummy
![Django ACC1](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/acc1.png)
![Django ACC2](https://github.com/CrysandyaVic/akikasik/blob/main/bagan/acc2.png)


# TUGAS 5

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, urutan prioritas atau specificity menentukan selector mana yang akan diterapkan ketika ada beberapa selector yang cocok untuk elemen yang sama. Berikut adalah urutan prioritas pengambilan CSS selector:
 1. **Inline Styles**: CSS yang ditulis langsung pada elemen HTML menggunakan atribut style memiliki prioritas tertinggi.
 2. **ID Selectors**: Selector yang menggunakan ID memiliki prioritas tinggi. ID selector ditulis dengan tanda pagar (#).
 3. **Class, Attribute, dan Pseudo-class Selectors**: Selector yang menggunakan class, atribut, atau pseudo-class memiliki prioritas lebih rendah daripada ID. Class selector ditulis dengan tanda titik (.).
 4. **Element dan Pseudo-element Selectors**: Selector yang menggunakan nama elemen HTML atau pseudo-element memiliki prioritas terendah.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

**Responsive design** adalah elemen penting dalam pengembangan aplikasi web karena memastikan tampilan dan fungsi aplikasi bisa menyesuaikan dengan baik di berbagai ukuran layar, seperti desktop, tablet, dan ponsel. Intinya, pengguna bisa merasa nyaman menggunakan aplikasi tanpa harus repot mengubah ukuran atau geser ke sana-sini, apa pun perangkat yang mereka pakai.

1. **Pengalaman pengguna yang lebih baik**: Semua pengguna, entah itu dari desktop atau ponsel, bisa merasakan tampilan yang enak dilihat dan mudah digunakan.
2. **Meningkatkan SEO**: Google suka website yang responsif, karena memberikan pengalaman yang baik. Akibatnya, website bisa tampil lebih tinggi di hasil pencarian.
3. **Hemat biaya dan waktu**: Dengan satu desain yang bisa digunakan di semua perangkat, tidak perlu lagi membuat versi khusus untuk desktop dan mobile.
4. **Loading lebih cepat**: Desain responsif biasanya lebih ringan, sehingga aplikasi atau website bisa terbuka lebih cepat di perangkat apa pun.

Contoh yang menerapkan responsive design :
1. Spotify
2. Instagram

Contoh yang **belum** menerapkan responsive design :
1. Craiglist
2. PWS

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
**Margin**
* Margin adalah ruang di **luar** batas elemen. Margin digunakan untuk memberikan jarak antara elemen satu dengan elemen lainnya. Margin tidak mempengaruhi ukuran elemen itu sendiri.
```
.element {
  margin: 20px; /* Memberikan margin 20px di semua sisi */
}
```


**Border**
* Border adalah **garis** yang mengelilingi elemen. Border berada di antara margin dan padding. Border dapat diatur ketebalan, gaya, dan warnanya.

```
.element {
  border: 2px solid black; /* Border hitam dengan ketebalan 2px */
}
```

**Padding**
* Padding adalah ruang di **dalam** batas elemen, antara konten elemen dan border. Padding digunakan untuk memberikan jarak di sekitar konten elemen.
```
.element {
  padding: 10px; /* Memberikan padding 10px di semua sisi */
}
```


## Jelaskan konsep flex box dan grid layout beserta kegunaannya!

**Flexbox (Flexible Box Layout)** adalah metode tata letak satu dimensi yang digunakan untuk mengatur elemen dalam satu baris atau kolom. Flexbox sangat berguna untuk membuat tata letak yang fleksibel dan responsif. Flexbox sangat cocok untuk tata letak yang memerlukan penyesuaian dinamis, seperti menu navigasi, galeri gambar, atau tata letak kartu. 

Berikut adalah beberapa fitur utama Flexbox:

1. **Arah Fleksibel**: Elemen dapat diatur dalam arah horizontal (baris) atau vertikal (kolom) menggunakan properti `flex-direction`.
Penjajaran dan Distribusi: Elemen dapat dijajarkan dan didistribusikan dengan mudah menggunakan properti seperti `justify-content`, `align-items`, dan `align-content`.
2. **Ukuran Fleksibel**: Elemen dapat tumbuh atau menyusut untuk mengisi ruang yang tersedia menggunakan properti `flex-grow`, `flex-shrink`, dan `flex-basis`.
3. **Urutan Elemen**: Urutan elemen dapat diubah tanpa mengubah urutan HTML menggunakan properti order.


**Grid Layout** adalah metode tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Grid Layout sangat berguna untuk membuat tata letak yang lebih kompleks dan terstruktur. Grid Layout sangat cocok untuk tata letak halaman yang kompleks seperti dashboard, halaman utama situs web, atau tata letak majalah. 

Berikut adalah beberapa fitur utama Grid Layout:

1. **Definisi Grid**: Grid didefinisikan menggunakan properti ```display: grid``` dan ```grid-template-rows``` serta `grid-template-columns` untuk menentukan ukuran baris dan kolom.
2. **Penempatan Elemen**: Elemen dapat ditempatkan di area grid tertentu menggunakan properti seperti `grid-row`, `grid-column`, `grid-area`.
3. **Jarak Antar Elemen**: Jarak antar elemen dapat diatur menggunakan properti `grid-gap` atau `gap`.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

### Menambah Tailwind
1. Menambah sebuah script CDN pada `base.html`pada bagian head
```
{% endblock meta %}
<script src="https://cdn.tailwindcss.com">
</script>

```

### Membuat fungsi edit dan delete product
1. Membuat 2 fungsi pada `views.py` yang bernama `edit_product` dan `delete_product`
```
def edit_product(request, id):
    # Get mood entry berdasarkan id
    product = Products.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = Products.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

```

2. Menambah import pada `views.py`
```
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect

```
3. Mengupdate `urls.py` agar bisa mengakses kedua fungsi baru tersebut dengan import dan menambah urlpatterns
```
from main.views import edit_product
from main.views import delete_product

urlpatters :
...
path('edit-product/<uuid:id>', edit_product, name='edit_product'),
path('delete/<uuid:id>', delete_product, name='delete_product'),

```

### Styling setiap page

1. **Halaman Login** : memodifikasi login.html agar bisa memuat gambar
```
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="bg-sky-100 flex justify-center items-center h-screen">
  <!-- Left: Image -->
  <div class="w-1/2 h-screen hidden lg:block">
    <img src="https://i.pinimg.com/564x/7c/87/61/7c8761a22815c393c90e4a16a3f130a1.jpg" alt="Placeholder Image" class="object-cover w-full h-full">
  </div>

  <!-- Right: Login Form -->
  <div class="lg:p-36 md:p-52 sm:20 p-8 w-full lg:w-1/2">
    <h1 class="text-2xl font-semibold mb-4">Login to AkikAsik</h1>
    <form action="" method="POST" class="space-y-6">
      {% csrf_token %}
      <div class="mb-4">
        <label for="username" class="block text-gray-600">Username</label>
        <input type="text" id="username" name="username" required class="w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500" autocomplete="off">
      </div>
      <div class="mb-4">
        <label for="password" class="block text-gray-800">Password</label>
        <input type="password" id="password" name="password" required class="w-full border border-gray-300 rounded-md py-2 px-3 focus:outline-none focus:border-blue-500" autocomplete="off">
      </div>
      <button type="submit" class="bg-red-500 hover:bg-blue-600 text-white font-semibold rounded-md py-2 px-4 w-full">
        Login
      </button>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      {% if message.tags == "success" %}
            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% elif message.tags == "error" %}
            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% else %}
            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                <span class="block sm:inline">{{ message }}</span>
            </div>
        {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <div class="mt-6 text-green-500 text-center">
      <a href="{% url 'main:register' %}" class="hover:underline">Sign up Here</a>
    </div>
  </div>
</div>
{% endblock content %}
```

2. **Halaman Register** : Memodifikasi register.html
```
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full space-y-8 form-style">
    <div>
      <h2 class="mt-6 text-center text-3xl font-extrabold text-black font-sans">
        Create your account
      </h2>
    </div>
    <form class="mt-8 space-y-6" method="POST">
      {% csrf_token %}
      <input type="hidden" name="remember" value="true">
      <div class="rounded-md shadow-sm -space-y-px">
        {% for field in form %}
          <div class="{% if not forloop.first %}mt-4{% endif %}">
            <!-- Centered label with text-center -->
            <label for="{{ field.id_for_label }}" class="block text-center mb-2 font-semibold text-black font-sans">
              {{ field.label }}
            </label>
            <div class="relative">
              {{ field }}
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                {% if field.errors %}
                  <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                  </svg>
                {% endif %}
              </div>
            </div>
            {% if field.errors %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            {% endif %}
          </div>
        {% endfor %}
      </div>

      <div>
        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 transition-all duration-200">
          Register
        </button>
      </div>
    </form>

    {% if messages %}
    <div class="mt-4">
      {% for message in messages %}
      <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
        <span class="block sm:inline">{{ message }}</span>
      </div>
      {% endfor %}
    </div>
    {% endif %}

    <div class="text-center mt-4">
      <p class="text-sm text-black font-sans">
        Already have an account?
        <a href="{% url 'main:login' %}" class="font-medium text-red-600 hover:text-red-800">
          Login here
        </a>
      </p>
    </div>
  </div>
</div>
{% endblock content %}
```

3. **Halaman Utama** : Memodif halaman utama agar bisa menampilkan card user dan product

`main.html`
```
{% extends 'base.html' %}
{% load static %}
{% block content %}
{% include 'navbar.html' %}


<div class="pt-16 max-w-7xl mx-auto">

    <!-- Wrap the user card in a flex container to center it -->
    <div class="flex justify-center items-center">
        {% include 'card_info.html' with namaMahasiswa=namaMahasiswa npm=npm kelas=kelas %}
    </div>

    <!-- Product section -->
    {% if not product_form %}
    <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/gambar-sedih.png' %}" alt="No products available" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">Belum ada data batu pada akikasik.</p>
    </div>
    {% else %}
      <!-- Check if there is only 1 product and center it accordingly -->
      {% if product_form|length == 1 %}
        <!-- Center the product when there is only one product -->
        <div class="flex justify-center mt-4">
          {% for product_entry in product_form %}
            {% include 'card_product.html' %}
          {% endfor %}
        </div>
      {% else %}
        <!-- Use grid layout when there are multiple products -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
          {% for product_entry in product_form %}
            {% include 'card_product.html' %}
          {% endfor %}
        </div>
      {% endif %}
    {% endif %}

    <!-- Buttons for adding product and logging out -->
    <div class="flex justify-center mt-8">
      <a href="{% url 'main:create_product_entry' %}">
        <button class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-lg">
          Add New Product Entry
        </button>
      </a>
    </div>

    <!-- Box for Last Login -->
    <div class="mt-6 flex justify-center">
      <div class="bg-gray-100 border border-gray-300 p-4 rounded-lg text-center shadow-md">
        <h5 class="font-semibold">Sesi terakhir login:</h5>
        <p class="text-gray-600">{{ last_login }}</p>
      </div>
    </div>
</div>
{% endblock content %}

```

`card_info.html`

```
<div class="w-full max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 my-4 p-6"> 
    <div class="flex flex-col items-center pb-10">
       
        <div class="p-2"> 
            <img class="w-24 h-24 mb-3 rounded-full shadow-lg" src="https://i.pinimg.com/564x/09/21/fc/0921fc87aa989330b8d403014bf4f340.jpg" alt="User Image"/>
        </div>

        <h5 class="mb-1 text-2xl font-bold text-gray-900 dark:text-white">{{ namaMahasiswa }}</h5>
       
        <span class="text-lg text-gray-600 dark:text-gray-300">NPM: {{ npm }}</span>
        <span class="text-lg text-gray-600 dark:text-gray-300">Kelas: {{ kelas }}</span>
    </div>
</div>
```

`card_product.html`

```
<div class="bg-white shadow-md rounded-lg overflow-hidden mb-4"> <!-- Use mb-4 for consistent spacing -->
    <div class="bg-gray-100 px-4 py-2 border-b border-gray-300">
        <h3 class="text-xl font-semibold text-gray-800">{{ product_entry.nama }}</h3>
    </div>

    <div class="p-4">
        <p class="text-gray-700 mb-4">{{ product_entry.deskripsi }}</p>
        <p class="text-indigo-600 text-lg font-semibold mb-4">Rp {{ product_entry.harga }}</p>

        <div class="flex space-x-4">
            <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Edit</a>
            <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Delete</a>
        </div>
    </div>
</div>
```


4. **Halaman edit dan tambah product** :
`create_product_entry.html`
```
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}

<div class="pt-16 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold text-center mb-6">Add New Product Entry</h1>

    <!-- Form container with padding and centered layout -->
    <form method="POST" class="bg-white shadow-md rounded-lg px-8 pt-6 pb-8 mb-4">
        {% csrf_token %}
        <div class="overflow-x-auto">
            <table class="table-auto w-full border-separate border-spacing-4">
                <!-- Render form fields with Tailwind CSS styling -->
                {{ form.as_table }}
                <tr>
                    <td class="pt-4"></td>
                    <td class="pt-4">
                        <!-- Styled submit button -->
                        <input type="submit" value="Add Product Entry" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg cursor-pointer">
                    </td>
                </tr>
            </table>
        </div>
    </form>
</div>

{% endblock %}
```


`edit_product.html`
```
<div class="bg-white shadow-md rounded-lg overflow-hidden mb-4"> <!-- Use mb-4 for consistent spacing -->
    <div class="bg-gray-100 px-4 py-2 border-b border-gray-300">
        <h3 class="text-xl font-semibold text-gray-800">{{ product_entry.nama }}</h3>
    </div>

    <div class="p-4">
        <p class="text-gray-700 mb-4">{{ product_entry.deskripsi }}</p>
        <p class="text-indigo-600 text-lg font-semibold mb-4">Rp {{ product_entry.harga }}</p>

        <div class="flex space-x-4">
            <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Edit</a>
            <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300">Delete</a>
        </div>
    </div>
</div>
```
5. **Navbar** : pada folder templates di root direktori, buat `navbar.html` yang berisi
```
<nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-full">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      
      <div class="flex-shrink-0">
        <h1 class="text-2xl font-bold text-white">AkikAsik</h1>
      </div>

     
      <div class="hidden md:flex items-center space-x-4">
        {% if user.is_authenticated %}
          <span class="text-white">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg mr-2">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg">
            Register
          </a>
        {% endif %}
      </div>

      <!-- Mobile menu button (visible on small screens) -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>

<!-- Script to toggle mobile menu visibility -->
<script>
  const btn = document.querySelector("button.mobile-menu-button");
  const menu = document.querySelector(".mobile-menu");

  btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
</script>
```

 ## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Penggunaan JavaScript dalam pengembangan aplikasi web memiliki beberapa manfaat yang signifikan, antara lain:

1. **Aplikasi web semakin interaktif**: JavaScript memungkinkan pengembang menambahkan interaksi dinamis pada situs web, seperti pop-up, animasi, validasi formulir secara real-time, dan efek visual lainnya. Ini membantu meningkatkan pengalaman pengguna.

2. **Kecepatan Eksekusi di Sisi Klien**: JavaScript dijalankan di browser pengguna (client-side), sehingga tidak perlu menunggu respons dari server untuk melakukan perubahan kecil, yang meningkatkan kecepatan eksekusi dan responsivitas aplikasi.

3. **Kompatibilitas Multi-Platform**: JavaScript dapat digunakan di berbagai perangkat dan browser. Selain itu, JavaScript modern mendukung pengembangan aplikasi berbasis web yang responsif, baik di desktop maupun perangkat mobile.
 
 ## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Fungsi dari penggunaan await ketika menggunakan fetch() adalah untuk menunggu sampai promise yang dihasilkan oleh fetch() selesai (resolved), yaitu ketika data yang diminta telah berhasil diambil dari server atau ketika ada kesalahan yang terjadi. Dengan menggunakan await, JavaScript akan menunggu secara asynchronous hingga permintaan tersebut selesai dan menghasilkan respons sebelum melanjutkan eksekusi baris kode berikutnya. Ini memastikan bahwa respons dari server diterima dan dapat diproses secara tepat sebelum melanjutkan ke langkah selanjutnya.

Jika await tidak digunakan, JavaScript tidak akan menunggu hasil dari fetch(), sehingga fetch() akan mengembalikan promise yang belum selesai (pending), yang bisa mengakibatkan data tidak tersedia saat kode mencoba mengaksesnya, karena eksekusi dilanjutkan langsung tanpa menunggu hasil fetch().

 ## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
 Decorator csrf_exempt digunakan pada view yang menerima AJAX POST untuk menonaktifkan pemeriksaan CSRF token yang secara default diaktifkan oleh Django. Ini diperlukan jika permintaan AJAX tidak menyertakan CSRF token, karena tanpa token tersebut, Django akan memblokir permintaan dan mengembalikan error 403 Forbidden.

Alasan Penggunaan:
Kemudahan Pengujian: Selama pengembangan, csrf_exempt memudahkan pengujian tanpa harus menangani CSRF token.
Permintaan dari Aplikasi Eksternal: Jika aplikasi pihak ketiga atau eksternal tidak menyertakan CSRF token, menggunakan csrf_exempt memungkinkan permintaan tersebut tetap diproses.


 ## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

Pembersihan data di backend tetap perlu dilakukan meskipun sudah ada validasi di frontend karena:

1. Keamanan: Frontend mudah dimanipulasi oleh pengguna melalui developer tools atau skrip eksternal. Tanpa pembersihan di backend, aplikasi rentan terhadap serangan seperti XSS atau SQL Injection, sehingga backend harus memastikan semua data aman sebelum diproses.

2. Konsistensi dan Kontrol: Pembersihan di backend memastikan bahwa data selalu melalui jalur validasi yang sama untuk semua pengguna, terlepas dari browser atau perangkat yang digunakan. Ini mencegah inkonsistensi dan memastikan integritas data yang masuk.

3. Lapisan Perlindungan: Backend adalah lapisan terakhir dalam memastikan validitas data. Jika pembersihan hanya dilakukan di frontend, ada risiko input berbahaya dapat mencapai server. Validasi di kedua sisi memberikan perlindungan ganda terhadap eksploitasi.

4. Logika Utama: Backend bertanggung jawab atas pengelolaan logika utama, seperti penyimpanan data di database. Memastikan data yang diterima aman dan sesuai sangat penting untuk menjaga keandalan aplikasi.
 
 ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

### 1. **Membuat Fungsi untuk Menambahkan Produk dengan AJAX**
   - Buat fungsi JavaScript yang mengambil data inputan dari pengguna seperti **nama**, **harga**, dan **deskripsi produk**.
   - Fungsi ini akan mengirimkan data tersebut ke server menggunakan `POST` request dengan **Fetch API**.
   - Data akan dikirimkan dalam format `FormData` melalui request `POST`, dan setelah sukses, modal ditutup dan data produk di-refresh tanpa reload halaman.

### 2. **Melakukan Routing**
   - **Import** fungsi yang sudah dibuat di views ke dalam `urls.py` untuk menangani request penambahan produk baru.
   - Tambahkan **urlpatterns** yang menghubungkan URL dengan fungsi view untuk menambahkan produk dengan AJAX. Pastikan routing ini menangani permintaan `POST`.

### 3. **Mengubah Cara Menampilkan Data**
   - **Hapus** atribut `productform` pada fungsi `views.py` yang sebelumnya digunakan untuk render form, karena sekarang data produk akan di-fetch dari endpoint JSON.
   - Pada fungsi `show_json` dan `show_xml`, ubah nilai dari `data` menjadi `Products.objects.filter(user=request.user)` agar hanya menampilkan produk dari pengguna saat ini.
   - **Ubah struktur HTML** di `main.html` untuk menghapus conditional blocks yang menampilkan produk secara langsung. Gantikan dengan `<div>` yang memiliki `id` sebagai placeholder di mana produk akan ditampilkan secara dinamis.
   
### 4. **Fetching dan Menampilkan Data Produk Asinkron**
   - **Buat dua fungsi** dalam blok `<script>`:
     - **getProductEntries()**: Fungsi ini bertugas untuk melakukan **fetch** data JSON dari endpoint yang sudah dibuat, lalu melakukan parsing data menjadi objek JavaScript.
     - **refreshProductEntries()**: Fungsi ini digunakan untuk mengambil data yang sudah di-fetch dan menampilkannya di halaman secara asinkron (tanpa reload). Produk akan ditampilkan dalam elemen HTML yang sudah dibuat di langkah sebelumnya.

### 5. **Mencegah XSS dengan Backend dan Frontend Proteksi**
   - Gunakan **strip_tags** pada backend (`views.py`) untuk memastikan bahwa input pengguna tidak mengandung tag HTML atau JavaScript berbahaya.
   - Tambahkan **DOMPurify** pada frontend untuk membersihkan data yang diambil dari server sebelum ditampilkan di halaman, sehingga lebih aman dari serangan XSS.

### Hasil Akhir:
- Ketika pengguna menambahkan produk baru melalui modal form, data akan dikirimkan ke server dengan **AJAX** tanpa perlu reload halaman.
- Produk baru akan muncul secara dinamis di halaman setelah penambahan data berhasil.
- Sistem sudah terlindungi dari serangan XSS di backend dan frontend.






# TUGAS 7

## Jelaskan apa yang dimaksud dengan stateless widget dan stateful widget, dan jelaskan perbedaan dari keduanya.
1. **Stateless Widget** : widget yang tidak memiliki state atau keadaan yang bisa berubah. Artinya, setelah widget ini tampil di layar, tampilan dan isinya tidak akan berubah selama widget tersebut aktif. Contoh dari Stateless Widget ini adalah widget Text, Icon, dan Container.

2. **Stateful Widget** : widget yang memiliki state atau keadaan yang bisa berubah selama aplikasi berjalan. Berbeda dengan Stateless Widget, Stateful Widget dapat memperbarui tampilannya ketika terjadi perubahan pada state di dalamnya. Contoh dari Stateful Widget antara lain Checkbox, TextField, dan AnimatedContainer.

## Sebutkan widget apa saja yang kamu gunakan pada proyek ini dan jelaskan fungsinya.
## Apa fungsi dari `setState()`? Jelaskan variabel apa saja yang dapat terdampak dengan fungsi tersebut.
Fungsi `setState()` digunakan dalam `StatefulWidget` untuk memperbarui state (keadaan) dari widget tersebut. Ketika `setState()` dipanggil, Flutter akan merender ulang tampilan atau widget yang terkait, sehingga perubahan state bisa terlihat di layar.

`setState()` hanya mempengaruhi variabel-variabel atau nilai yang termasuk dalam kelas State dari `StatefulWidget`. Semua variabel yang diubah atau diperbarui dalam `setState()` akan berdampak pada tampilan widget tersebut, tapi tidak akan mempengaruhi widget lainnya di luar StatefulWidget yang sedang diperbarui.

## Jelaskan perbedaan antara const dengan final.
const:

const digunakan untuk membuat variabel yang bersifat konstan dan diinisialisasi secara langsung pada saat compile time (waktu kompilasi). Ini berarti nilai dari variabel const harus sudah diketahui dan tetap saat kode dikompilasi.
const biasanya digunakan untuk nilai-nilai konstan yang sederhana seperti angka, string, atau objek yang bisa dibuat pada saat kompilasi.
const bisa dipakai di kelas maupun dalam pembuatan widget untuk meningkatkan efisiensi, karena const widget dianggap "immutable" (tidak bisa diubah) dan tidak perlu dirender ulang.
Contoh:
dart
Copy code
const pi = 3.14159;
const textWidget = Text("Hello, world!", style: TextStyle(fontSize: 20));
final:

final digunakan untuk variabel yang hanya bisa diinisialisasi satu kali, tetapi nilainya bisa ditentukan pada saat runtime (waktu aplikasi berjalan). Jadi, variabel final tidak harus diketahui nilainya pada saat kompilasi.
final biasanya digunakan ketika kita ingin sebuah variabel tidak bisa diubah setelah nilai pertamanya diatur, namun nilai itu mungkin baru tersedia saat aplikasi berjalan, seperti hasil dari API atau operasi yang bergantung pada waktu eksekusi.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist-checklist di atas.