# Todo List

[Link menuju aplikasi Heroku](https://assignment2-django-swas.herokuapp.com/todolist/)

## Apa perbedaan dari Inline, Internal, dan External CSS?

Perbedaan dari segi cara penulisan:
- Inline CSS ditulis di dalam tag HTML sebagai atrribute. Keyword dari attribute-nya adalah `style`. Contoh `<p style="color:black;"> Halo </p>`
- Internal CSS di dalam tag `<style>` pada blok `<head>`. CSS bisa langsung ditulis seperti syntax aslinya.
- Eksternal CSS dibuat dengan file CSS yang nantinya diimport ke dalam file HTML. Meng-import file CSS ini dilakukan di dalam tag `<link>`

Keuntungan dan kelemahan:
- Inline CSS mudah digunakan untuk melakukan styling hanya pada objek tertentu.
- Internal CSS cocok digunakan untuk melakukan styling yang sama pada satu file HTML.
- Eksternal CSS baik untuk melakukan styling yang sama pada banyak objek di banyak file yang berbeda.

## Macam-macam Tag HTML5

- `<h1>` sampai `<h6>` digunakan untuk membuat header. 
- `<p>` digunakan untuk membuat elemen teks
- `<style>` digunakan sebagai tempat menaruh internal CSS
- `<a>` digunakan untuk membuat elemen yang dapat mengarah ke reference lain
- `<button>` digunakan untuk membuat tombol
- `<div>` biasanya digunakan untuk membuat container

## Tipe-tipe CSS selector

- Class selector, digunakan untuk melakukan styling terhadap keseluruhan class. Contoh penulisannya adalah `.class {}`
- Id selector, digunakan untuk melakukan styling terhadap suatu elemen dengan id yang sesuai. Id harus bersifat unik. Contoh penulisannya adalah `#id {}`
- Tag selector, digunakan untuk melakukan styling terhadap keseluruhan elemen dengan tag yang bersangkutan. Contoh penulisannya adalah `tag {}`

## Cara Implementasi

1. Menginstall django-tailwind ke project Django. Referensi ada pada [link ini](https://django-tailwind.readthedocs.io/en/latest/installation.html)

2. Menerapkan styling untuk masing-masing template, yaitu `todolist.html`, `login.html`, `register.html`, dan `create_task.html`

3. Membuat navbar pada halaman utama todolist

4. Membuat card untuk masing-masing task yang telah dibuat