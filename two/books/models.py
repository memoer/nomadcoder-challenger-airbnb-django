import datetime
from django.db import models
from core import models as core_models
from categories import models as categories_models
from people import models as people_models
"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""


class Book(core_models.TimeStampedModel):
    def year_choices():
        return [(r, r) for r in range(1950, datetime.date.today().year + 1)]

    def current_year():
        return datetime.date.today().year

    def rating_choices():
        return [(r, r) for r in range(1, 10)]

    title = models.CharField(max_length=128)
    year = models.IntegerField(
        'year', choices=year_choices(), default=current_year())
    category = models.ForeignKey(categories_models.Category, on_delete = models.SET_NULL,null=True, related_name="book_category")
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField('rating', choices=rating_choices(), default=1)
    wrtier = models.ForeignKey(people_models.Person, on_delete = models.CASCADE)
    def __str__(self):
      return self.title
