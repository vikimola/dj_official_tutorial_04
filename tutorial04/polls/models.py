# Create your models here.
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Choice(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    vote_num = models.IntegerField(default=0)
