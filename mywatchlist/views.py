from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_watchlist_html(request):
    data = MyWatchList.objects.all()
    context = {
        'watchlist': data,
        'name': 'Made Swastika Nata Negara',
        'id' : '2106630095',
    }
    return render(request, "watchlist.html", context)

def show_watchlist_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")