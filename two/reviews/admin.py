from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
  list_display=(
    "created_by",
    "text",
    "movie",
    "book",
    "rating",
  )
  list_filter = (
    "created_by",
    "movie",
    "book"
  )
  search_fields = ("text",)