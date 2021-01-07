from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
  list_display = (
    "title",
    "year",
    "category",
    "cover_image",
    "rating",
    "wrtier",
  )
  list_filter = (
    "title",
    "category",
    "wrtier",
  )
  search_fields = ("title",)