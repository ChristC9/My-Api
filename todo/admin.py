from django.contrib import admin

from .models import ToDo

# Register your models here.

class adminToDo(admin.ModelAdmin):
    list_display=('name','title','date','completed')


admin.site.register(ToDo,adminToDo)