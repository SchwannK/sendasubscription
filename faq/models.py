from django.db import models

# Create your models here.

class FaqCategory(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name or self.reference

class FaqEntry(models.Model):

    category = models.ForeignKey(FaqCategory)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question
