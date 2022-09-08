from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=200)

class Location(models.Model):
    name = models.CharField(max_length=200)
    distance_air = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image/',height_field=None,width_field=None)
    check_tur = models.BooleanField(default=False)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Kind_transport(models.Model):
    name = models.CharField(max_length=200)
    quantity_place = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Route(models.Model):
    time = models.TimeField()
    num_tran = models.IntegerField()
    description = models.TextField()
    check_tur = models.BooleanField(default=False)
    kind_tran = models.ForeignKey(Kind_transport, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Kind_transport(models.Model):
#     name = models.CharField(max_length=200)
#     quantity_place = models.IntegerField()
#     price = models.IntegerField()

class Food(models.Model):
    kitchen=models.TextField()
    description = models.TextField()
    price_day = models.CharField(max_length=300)
    check_tur = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    home = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Housing(models.Model):
    name = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    pic_cart = models.ImageField(upload_to='image/',height_field=None,width_field=None)
    url = models.URLField(max_length=500)
    price = models.CharField(max_length=300)
    check_tur = models.BooleanField(default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




