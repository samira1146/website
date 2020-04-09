from django.contrib import admin

# Register your models here.
from .models import Designer,Jornal, Article

admin.site.register(Designer)
admin.site.register(Jornal)
admin.site.register(Article)
