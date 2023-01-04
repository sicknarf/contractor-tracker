from django.contrib import admin
from main_app.models import Client, Task

# Register your models here.
admin.site.register(Client)
admin.site.register(Task)