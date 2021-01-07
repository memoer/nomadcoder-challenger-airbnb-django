from django.db import models
from core import models as core_models
from users import models as users_models
from books import models as books_models
from movies import models as movies_models

"""
Here are the models you have to create:
- FavList
  created_by (OneToOne => users.User)
  books (ManyToMany => books.Book)
  movies (ManyToMany => movies.Movie)
"""
class FavList(core_models.TimeStampedModel):
  created_by = models.OneToOneField(users_models.User, on_delete=models.CASCADE)
  books = models.ManyToManyField(books_models.Book)
  movies = models.ManyToManyField(movies_models.Movie)
  def __str__(self):
    return f"created_by:{self.created_by}"