from django.db import models

# Create your models here.
class donation(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField( max_length=50)
    mail=models.EmailField(max_length=254,default="none@gmail.com")
    amount=models.IntegerField()
    date_paid=models.DateTimeField(auto_now_add=True)
    payment_id=models.CharField(max_length=50)
    order_id=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    