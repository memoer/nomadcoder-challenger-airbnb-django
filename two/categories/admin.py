from django.contrib import admin
from . import models

"""
Here are the models you have to create:

"""
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = (
    "name",
    "kind",
  )
  list_filter = (
    "kind",
  )
  search_fields = ("name",)