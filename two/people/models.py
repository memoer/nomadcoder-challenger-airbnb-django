from django.db import models
from core import models as core_models

"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""
class Person(core_models.TimeStampedModel):
    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=128)
    kind = models.CharField(max_length=8, choices=KIND_CHOICES, default=KIND_ACTOR)
    photo = models.ImageField(blank=True)
    def __str__(self):
      return self.name