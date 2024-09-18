from django.contrib import admin
from .models import Information_Contact, MessageFromCustomer, Subscriber


# Register your models here.
admin.site.register(Information_Contact)
admin.site.register(MessageFromCustomer)
admin.site.register(Subscriber)