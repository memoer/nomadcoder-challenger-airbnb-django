from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_KOREAN, "Korean"))
    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"
    PREFERENCE_CHOICES = ((PREFERENCE_BOOKS, "Books"), (PREFERENCE_MOVIES, "Movies"))
    bio = models.TextField(default="")

    preference = models.CharField(
        choices=PREFERENCE_CHOICES, max_length=6, default=PREFERENCE_BOOKS
    )

    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=7, default=LANGUAGE_KOREAN
    )

    favourite_book_genere = models.CharField(max_length=12, default="any")
    favourite_movies_genere = models.CharField(max_length=12, default="any")
