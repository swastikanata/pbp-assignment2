from django.test import TestCase
from katalog.models import CatalogItem

class TestModels(TestCase):
        
    def test_models(self):
        CatalogItem.objects.create(
            item_name="Kemeja", 
            item_price=399000, 
            item_stock=1, 
            description="Kemeja stylish dengan bahan yang nyaman di kulit", 
            rating=4.2, 
            item_url="https://www.uniqlo.com/id/id/products/E444645-000?colorCode=COL32&sizeCode=SMA006&gclid=Cj0KCQjw94WZBhDtARIsAKxWG-_SEfMjpHi6dea6_wLHlSKmntKenb908sa9E_aDQ-ZTUk5DxSOWO4UaAkjSEALw_wcB"
        )
        laptop = CatalogItem.objects.get(item_name="Kemeja")
        
        self.assertEquals(
            laptop.item_name, 
            "Kemeja",
        )