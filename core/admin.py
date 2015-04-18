from django.contrib import admin

# Register your models here.
from .models import Recipient, GiftCard, Category

admin.site.register(Recipient)
admin.site.register(Category)
admin.site.register(GiftCard)
