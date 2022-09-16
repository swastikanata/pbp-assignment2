from django.urls import path

from mywatchlist.views import show_watchlist_html
from mywatchlist.views import show_watchlist_xml
from mywatchlist.views import show_watchlist_json
# from mywatchlist.views import show_catalog

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist_html, name='show_catalog'),
    path('html/', show_watchlist_html, name='show_catalog'),
    path('xml/', show_watchlist_xml, name='show_catalog'),
    path('json/', show_watchlist_json, name='show_catalog'),
]