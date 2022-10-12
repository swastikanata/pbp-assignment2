# Todo List - 2

[Link menuju aplikasi Heroku](https://assignment2-django-swas.herokuapp.com/todolist/)

## Perbedaan antara _asynchronous programming_ dengan _synchronous programming_
Synchronus programming adalah konsep pemrograman di mana kode dieksekusi secara berurutan sehingga pengguna harus menunggu data selesai diproses terlebih dahulu sebelum melakukan interaksi selanjutnya. Asynchronus programming adalah konspep pemrograman di mana kode dapat dieksekusi secara paralel sehingga pengguna tidak diharuskan untuk menunggu data selesai diproses sebelum lanjut ke interaksi selanjutnya karena beberapa pemrosesan dapat dilakukan secara bersamaan.

## Paradigma _Event-Driven Programming_
Event-driven programming adalah salah satu paradigma pemrograman di mana alur jalannya program yang dibuat banyak ditentukan oleh event, misalnya interaksi yang dilakukan oleh user. Event tersebut misalnya mengeklik tombol, menggerakan mouse, dll. Paradigma ini umumnya digunakan dalam aplikasi yang banyak menerima input dari user. Contoh penerapan event-driven programming dalam tugas ini adalah implementasi tombol penambahan task. Ketika tombol ditekan, akan muncul  modal agar user bisa membuat task baru.

## Penerapan _asynchronous programming_ pada AJAX
AJAX merupakan suatu tool untuk menerapkan asynchronous programming pada halaman web. Dalam hal ini, AJAX dapat membuat halaman web ter-update secara asynchronous, yaitu browser tidak perlu untuk me-reload keseluruhan halaman web jika hanya sebagian kecil dari halaman web yang mengalami perubahan, cukup bagian tersebut saja yang di-update.

Membuat view serta url path baru yang mereturn sebuah response JSON. Implementasi asynchronous programming AJAX dalam tugas ini terdapat pada function get serta post untuk mengambil serta mengirim data JSON ke server, serta mengatur tampilan pada Todo list secara asynchronous sesuai data yang ada pada database

AJAX adalah salah satu cara menarapkan asychronus programming pada web dengan bahasa JavaScript. AJAX dapat digunakan untuk melakukan update pada halaman web secara asynchronus sehingga keseluruhan web tidak perlu di-reload apabila hanya dilakukan perubahan pada sebagian kecil halaman web. Misalnya, ketika ketika user membuat task baru, meng-update dan menghapus task, halaman web tidak perlu di-reload.

## Cara Implementasi
1. Membuat views baru yang dapat mereturn task-task yang sudah dibuat dalam format JSON
2. Menambahkan attribute onClick pada button untuk membuat, mengupdate, dan menghapus task menggunakan AJAX
3. Membuat function untuk membuat GET dan POST request ke server
4. Membuat modal untuk membuat task baru (menggantikan halaman HTML khusus untuk membuat task baru pada tugas 5). Ketika user mengklik tombol submit, modal otomatis ditutup dan halaman utama di-reload secara asynchronus