from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.

class TestViews(TestCase):

    def setUp(self):
        self.clent = Client()
        
    def test_views(self):
        url = reverse('mywatchlist:show_watchlist',)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    def test_views_html(self):
        url = reverse('mywatchlist:show_watchlist_html',)
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
    
    def test_views_xml(self):
        url = reverse('mywatchlist:show_watchlist_xml',)
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    def test_views_json(self):
        url = reverse('mywatchlist:show_watchlist_json',)
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)

    