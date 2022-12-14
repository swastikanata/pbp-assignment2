from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchListModel

# Create your views here.

def show_watchlist_index(request):
    watched_more_movies = MyWatchListModel.objects.filter(watched=True).count() >= MyWatchListModel.objects.filter(watched=False).count()
    context = {
        'watched_more': watched_more_movies,
    }
    return render(request, "watchlist_index.html", context)

def show_watchlist_html(request):
    data = MyWatchListModel.objects.all()
    watched_more_movies = MyWatchListModel.objects.filter(watched=True).count() >= MyWatchListModel.objects.filter(watched=False).count()
    context = {
        'watchlist': data,
        'watched_more': watched_more_movies,
        'name': 'Made Swastika Nata Negara',
        'id' : '2106630095',
    }
    return render(request, "watchlist.html", context)

def show_watchlist_xml(request):
    data = MyWatchListModel.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_watchlist_json(request):
    data = MyWatchListModel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")