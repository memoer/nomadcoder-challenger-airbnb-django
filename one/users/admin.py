from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
  list_display = (
    "username",
    "language",
    "preference",
    "favourite_book_genere",
    "favourite_movies_genere"
  )
  fieldsets = UserAdmin.fieldsets + (
    (
      "Custom",
      {
        "fields": (
          "bio",
          "preference",
          "language",
          "favourite_book_genere",
          "favourite_movies_genere"
          )
      }
    ),
  )
