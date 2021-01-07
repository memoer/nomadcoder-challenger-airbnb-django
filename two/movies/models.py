import datetime
from django.db import models
from core import models as core_models
from categories import models as categories_models
from people import models as people_models

"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""
class Movie(core_models.TimeStampedModel):
    def year_choices():
        return [(r, r) for r in range(1950, datetime.date.today().year + 1)]

    def current_year():
        return datetime.date.today().year

    def rating_choices():
        return [(r, r) for r in range(1, 10)]

    title = models.CharField(max_length=128)
    year = models.IntegerField(
        'year', choices=year_choices(), default=current_year())
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField('rating', choices=rating_choices(), default=1)
    category = models.ManyToManyField(categories_models.Category, related_name="movie_category")
    director = models.ForeignKey(people_models.Person, on_delete=models.CASCADE, related_name="movie_director")
    cast = models.ManyToManyField(people_models.Person, related_name="movie_cast")
    def __str__(self):
      return self.title