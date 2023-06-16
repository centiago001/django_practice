from django.contrib import admin
from contact_us.models import Enquery


class admin_panals(admin.ModelAdmin):
    list_display=('name','email','massage')

admin.site.register(Enquery,admin_panals)
# Register your models here.
