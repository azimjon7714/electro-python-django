from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    class Meta:
        model: Category

admin.site.register(Category, CategoryAdmin)
