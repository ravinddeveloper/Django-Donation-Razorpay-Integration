from django.contrib import admin
from .models import donation
# Register your models here.

class donation_class(admin.ModelAdmin):
    list_display=['name','phone','amount','date_paid','payment_id']

admin.site.register(donation, donation_class)