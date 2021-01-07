from django.db import models
from core import models as core_models
from users import models as users_models
from movies import models as movies_models
from books import models as books_models

"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""

class Review(core_models.TimeStampedModel):
  def rating_choices():
        return [(r, r) for r in range(1, 10)]

  created_by = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
  text = models.TextField()
  movie = models.ForeignKey(movies_models.Movie, on_delete=models.SET_NULL, null=True, blank=True)
  book = models.ForeignKey(books_models.Book, on_delete=models.SET_NULL, null=True, blank=True)
  rating = models.IntegerField('rating', choices=rating_choices(), default=1)
  def __str__(self):
    return f"created_by_{self.created_by}:{self.text[:8]}..."
