# Todo List

[Link menuju aplikasi Heroku](https://assignment2-django-swas.herokuapp.com/todolist/)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

`{% csrf_token %}` berguna untuk melindungi keamanan laman dari serangan CSRF Attack. Tanpa adanya token tersebut, form yang kita buat dapat diisi oleh pihak yang tidak terpercaya. Oleh karena itu, Django tidak mengizinkan kita mengakses alamat yang berisi form tanpa `{% csrf_token %}`.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }}`)?

Bisa. Caranya adalah dengan membuat elemen `<form>` yang diisi oleh input field sesuai kebutuhan kita dengan menggunakan elemen `<input>`. Terakhir, kita perlu menambahkan `<input type="submit">` untuk meng-submit form tersebut. Membuat elemen form secara manual memberikan keuntungan berupa fleksibilitas.

## Alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user menekan tombol bertipe submit, browser akan mengirimkan request dengan method POST untuk melakukan perubahan pada server atau database, misalnya membuat model sesuai dengan input yang diberikan oleh user dan menyimpannya ke database. Setelah hal tersebut berhasil dilakukan, user diarahkan kembali ke views yang sesuai untuk menampilkan data, termasuk data baru yang diinput oleh user sebelumnya.

## Cara Implementasi

1. Membuat aplikasi baru bernama `todolist`
    ```
    python manage.py startapp todolist
    ```

2. Masukkan aplikasi `todolist` ke `INSTALLED_APPS` pada `settings.py`
    ```
    INSTALLED_APPS = [
        .....,
        'todolist',
    ]
    ```

3. Membuat model baru bernama `Task` pada `models.py`
    ```
    class Task(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        date = models.DateField(auto_now=True)
        title = models.CharField(max_length=255)
        description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```

4. Lakukan migrasi
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Pada `views.py`, buat function yang dapat menerima request dan memberi response untuk masing-masing url yang akan dibuat
    ```
    @login_required(login_url='/todolist/login/')
    def show_todolist(request):
        ...

    @login_required(login_url='/todolist/login/')
    def create_task(request):
        ...
    
    def register_todolist(request):
        ...

    def login_todolist(request):
        ...
    
    def logout_todolist(request):
        ...
    
    @login_required(login_url='/todolist/login/')
    def update_todolist(request, id):
        ...

    @login_required(login_url='/todolist/login/')
    def delete_todolist(request, id):
        ...
    ```
 
6. Pada `urls.py` di `project_django` tambahkan url ke aplikasi todolist
    ```
    urlpatterns = [
        ...
        path('todolist/', include('todolist.urls')),
    ]
    ```

7. Pada `urls.py` di `todolist` tambahkan url yang sesuai untuk menerima data berupa HTML, XML, maupun json
    ```
    urlpatterns = [
        path('', show_todolist, name='show_todolist'),
        path('create-task/', create_task, name='create_task'),
        path('register/', register_todolist, name='register_todolist'),
        path('login/', login_todolist, name='login_todolist'),
        path('logout/', logout_todolist, name='logout_todolist'),
        path('update/<int:id>/', update_todolist, name='update_todolist'),
        path('delete/<int:id>/', delete_todolist, name='delete_todolist'),
    ]
    ```

8. Buat HTML file untuk proses menampilkan todolist, membuat todo baru, register, dan login.

9. Buat 2 akun dan masing-masing 3 dummy data pada akun masing-masing di situs web Heroku.
