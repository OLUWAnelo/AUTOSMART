from django.db import models
from datetime import datetime

# Create your models here.

class Car(models.Model):
    BRAND = (
        ('BMW', 'BMW'),
        ('Mercedez', 'Mercedez'),
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Nissan', 'Nissan'),
        ('Audi', 'Audi'),
    )

    TRANSMISSION = (
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    )


    YEAR= []
    for r in range(2000, (datetime.now().year+1)):
        YEAR.append((r,r))


    title = models.CharField(max_length = 250)
    model = models.CharField(max_length = 250)
    year = models.IntegerField(('year'), choices=YEAR)
    discounted_price = models.IntegerField()
    actual_price = models.IntegerField()
    description = models.TextField()
    car_photo1 = models.ImageField(upload_to='photo/%Y/%m/%d')
    car_photo2 = models.ImageField(upload_to='photo/%Y/%m/%d')
    car_photo3 = models.ImageField(upload_to='photo/%Y/%m/%d')
    car_photo4 = models.ImageField(upload_to='photo/%Y/%m/%d')
    milage = models.IntegerField()
    brand = models.CharField(choices=BRAND, max_length=50)
    transmission = models.CharField(choices=TRANSMISSION, max_length=50)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

