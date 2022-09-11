# Katalog

[Link menuju aplikasi Heroku](https://assignment2-django-swas.herokuapp.com/)

## Bagan

---

![Bagan](../static/Bagan.png?raw=true)
- HTTP request dibuat oleh user/client.
- Request dari user akan dihandle di `urls.py` untuk diarahkan ke views yang sesuai.
- Di `views.py ` akan dijalankan fungsi yang sudah dirancang sebelumnya. Apabila terdapat permintaan untuk mengakses database, hal tersebut akan dilakukan melalui `models.py`.
- `models.py` akan mengakses database sesuai query dari views dan mengembalikan data yang diinginkan.
- Template menyediakan file HTML yang kemudian akan dikirim kembali oleh views ke user sebagai HTTP Response.

## Virtual Environment

--- 

### Mengapa menggunakan virtual environment?

Virtual environment (lingkungan virtual) merupakan suatu development environment yang digunakan Django untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django. Hal ini dilakukan untuk agar perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya dan menyebabkan konflik antar satu program dengan program lain.

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Kita tetap bisa membuat aplikasi web berbasis Django tanpa virtual environment. Namun, karena tidak menggunakan virtual environment, artinya kita harus meng-install semua package yang dibutuhkan secara langsung ke komputer. Hal ini bukan merupakan *best practice* karena bisa saja mengganggu proyek lain yang menggunakan package atau dependencies dengan versi yang berbeda. 

## Cara Implementasi

---

### Poin 1

Membuat function bernama `show_katalog(request)` pada file `katalog/views.py`. Function tersebut akan menerima HTTP request dari user sebagai parameter. Function ini kemudian meminta semua data dari model `CatalogItem`. Function kemudian melakukan render file `template/katalog.html` dengan data yang diambil tadi sebagai `context`.

### Poin 2

Menambahkan `path('katalog/', include('katalog.urls'))` pada file `project_django/urls.py`.  Cantumkan route `'' (root)` yang dihubungkan ke fungsi `show_katalog(request)` pada `katalog/views.py`. 
Kemudian menambahkan `path('', show_catalog, name='show_catalog')` file `katalog/urls.py` untuk mengarahkan `route /katalog` ke function `show_catalog` pada file `katalog/views.py`.

### Poin 3

Menambahkan `{{nama}}` dan `{{id}}` pada file `katalog/templates/katalog.html` untuk menampilkan nama dan NPM sesuai dengan key yang dibuat pada context. Kemudian, lakukan looping untuk menampilkan semua isi dari `data_catalog_item` di dalam tabel.

### Poin 4

Buat app baru pada Heroku, kemudian tambahkan nama app heroku dan API Key Heroku pada repository secrets dengan key `HEROKU_APP_NAME` dan `HEROKU_API_KEY`. Jalankan kembali workflow yang gagal. Deployment berjalan sesuai dengan Actions yang sudah diatur oleh template tugas.