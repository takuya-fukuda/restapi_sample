from django.contrib import admin
from .models import Book, Weather

# Register your models here.
#adminで見れるようにDBを登録してあげる
admin.site.register(Book)
admin.site.register(Weather)
