from django.contrib import admin
from information import models


admin.site.register(models.Book,admin.ModelAdmin)
admin.site.register(models.Author,admin.ModelAdmin)