from django.contrib import admin

from .models import Challenge, Tag, Category

# Register your models here.
admin.site.register(Challenge)
admin.site.register(Tag)
admin.site.register(Category)