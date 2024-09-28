from django.db import models
from django.utils import timezone
import datetime  # Import datetime module
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)  # Add this line to define the question text
    pub_date = models.DateTimeField('date published')  # Field to store the publication date

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text  # Add a string representation for the Question model


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Link to Question
    choice_text = models.CharField(max_length=200)  # Field for choice text
    votes = models.IntegerField(default=0)  # Field for vote count

    def __str__(self):
        return self.choice_text  # Add a string representation for the Choice model
