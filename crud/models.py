from django.db import models

class Record(models.Model):
    order_date = models.DateField()
    shipping_date = models.DateField() 
    ship_mode = models.CharField(max_length=50)
    postal_code = models.IntegerField()
    region = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    sub_category = models.CharField(max_length=20)
    sales = models.IntegerField()
    quantity = models.IntegerField()
    profit = models.FloatField()
    order_rating = models.IntegerField()

    def __str__(self):
        return(f"{self.region} {self.postal_code}")