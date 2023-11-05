from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class fruitItem(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    fruitName = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='food_images/',  blank=True)  

    def __str__(self):
        return self.fruitName



# class fruitBooking(models.Model):
#     fruit_id = models.ForeignKey(fruitItem, on_delete=models.CASCADE)
#     fruit_name = models.CharField(max_length=255)
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     seller = models.CharField(max_length=255) 
#     fruit_requested = models.DecimalField(max_digits=5, decimal_places=2)
#     start_date = models.DateField()
#     contact_email = models.EmailField()
#     contact_phone = models.CharField(max_length=15)


#     def fruit_name(self):
#         return self.fruit_id.fruitName

class fruitBooking(models.Model):
    fruit_name = models.CharField(max_length=255)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    seller = models.CharField(max_length=255) 
    fruit_requested = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
