from django.contrib import admin
from .models import Question, Class, Choice, Quiz

# Register your models here.
admin.site.register(Class)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Quiz)

