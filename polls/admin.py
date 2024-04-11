from django.contrib import admin
from .models import Question,Choice
# Register your models here.


class ChoiceInLine(admin.TabularInline):
     model = Choice
     
    
class QuestionAdmin(admin.ModelAdmin):
     list_display = ["question_text","publish_date","was_published_recently"]
     fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["publish_date"], "classes" : ["collapse"]}),
    ]
     inlines = [ChoiceInLine]

admin.site.register(Question , QuestionAdmin)