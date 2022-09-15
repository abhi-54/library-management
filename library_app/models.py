from statistics import mode
from django.db import models

class Book(models.Model):
  book_name = models.CharField(max_length=20, null=False, blank=False)
  book_author = models.CharField(max_length=20, null=True, blank=True)

  def __str__(self):
    return self.book_name + ' - ' + self.book_author
