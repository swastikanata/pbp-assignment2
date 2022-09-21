# My Watchlist

[Link menuju aplikasi Heroku](https://assignment2-django-swas.herokuapp.com/mywatchlist/)

## Perbedaan antara JSON, XML, dan HTML

### JSON

- Fokus utamanya untuk mengirim data
- Menyimpan data dalam pasangan key dan value
- Ukuran data relatif kecil
- Bisa di-parse dengan fungsi JavaScript standar

### XML
- Merupakan markup language
- Fokus utamanya untuk mengirim data
- Menyimpan data dengan bentuk tree structure
- Ukuran data relatif lebih besar daripada JSON karena menggunakan tag
- Memerlukan XML parser untuk melakukan parsing

### HTML

- Merupakan markup language
- Fokus utamanya untuk menampilkan data
- Menyimpan data dengan bentuk tree structure


## Mengapa memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery mempermudah pertukaran data atau informasi antar aplikasi, bahkan yang dibangun di atas platform yang berbeda sekaligus.

## Cara Implementasi

1. Membuat aplikasi baru bernama `mywatchlist`
    ```
    python manage.py startapp mywatchlist
    ```

2. Masukkan aplikasi `mywatchlist` ke `INSTALLED_APPS` pada `settings.py`
    ```
    INSTALLED_APPS = [
        .....,
        'mywatchlist',
    ]
    ```

3. Membuat model baru bernama `MyWatchListModel` pada `models.py`
    ```
    class MyWatchListModel(models.Model):
        watched = models.BooleanField()
        title = models.CharField(max_length=255)
        rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
        release_date = models.CharField(max_length=255)
        review = models.TextField()
    ```

4. Lakukan migrasi
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Buat file json bernama `initial_watchlist_data.json` ke dalam folder `fixtures` dan masukkan data yang diperlukan. Load data dengan perintah berikut.
    ```
    python manage.py loaddata initial_watchlist_data.json
    ```

6. Pada `views.py`, buat function yang dapat menerima request dan memberi response untuk masing-masing url yang akan dibuat
    ```
    def show_watchlist_index(request):
        ...
        return render(request, "watchlist_index.html", context)

    def show_watchlist_html(request):
        ...
        return render(request, "watchlist.html", context)
    
    def show_watchlist_xml(request):
        ...
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_watchlist_json(request):
        ...
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
 
 7. Pada `urls.py` di `project_django` tambahkan url ke aplikasi mywatchlist
    ```
    urlpatterns = [
        ...
        path('mywatchlist/', include('mywatchlist.urls')),
    ]
    ```

 8. Pada `urls.py` di `mywatchlist` tambahkan url yang sesuai untuk menerima data berupa HTML, XML, maupun json
    ```
    urlpatterns = [
        path('', show_watchlist_index, name='show_watchlist'),
        path('html/', show_watchlist_html, name='show_watchlist_html'),
        path('xml/', show_watchlist_xml, name='show_watchlist_xml'),
        path('json/', show_watchlist_json, name='show_watchlist_json'),
    ]
    ```
    
## Postman

### JSON
![json](https://user-images.githubusercontent.com/68062339/191516493-8097fc66-f4c9-4c9e-adb8-7faf85445add.png)
### XML
![xml](https://user-images.githubusercontent.com/68062339/191516388-5116da0e-e06f-4c32-91ce-fa0f8dc4ac2e.png)
### HTML
![html](https://user-images.githubusercontent.com/68062339/191516268-c2b0c0cb-86c2-4440-8ad5-e3fbf4edd21d.png)