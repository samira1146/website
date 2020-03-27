from django.contrib import admin

# Register your models here.
from .models import SignUp,designer,jornal
admin.site.register(SignUp)
admin.site.register(designer)
admin.site.register(jornal)
