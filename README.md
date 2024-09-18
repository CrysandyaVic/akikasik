
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