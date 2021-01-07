from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Category
  name
  kind (book/movie/both)
"""


class Category(core_models.TimeStampedModel):
    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"
    KIND_CHOICES = (
        (KIND_BOOK, "BOOK"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )
    name = models.CharField(max_length=64)
    kind = models.CharField(
        max_length=6, choices=KIND_CHOICES, default=KIND_BOOK)
    def __str__(self):
      return self.name
