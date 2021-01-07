from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):
  list_display=(
    "created_by",
  )
  search_fields = ("created_by",)
  filter_horizontal = (
    "books",
    "movies",
  )