from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
  list_display=(
    "title",
    "year",
    "cover_image",
    "rating",
    "director",
  )
  list_filter = (
    "director",
  )
  search_fields = ("title",)
  filter_horizontal = (
    "category",
    "cast",
  )