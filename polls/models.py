import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField("date published")
    @admin.display(
            boolean = True,
            ordering="publish_date",
            description="Published recently?",
    )
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

    list_filter = ["publish_date"]
    search_fields = ["question_text"]

    def __str__(self) -> str:
        return self.question_text

class Choice (models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.choice_text
    
    