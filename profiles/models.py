from django.db import models
from users.models import CustomUser
from quiz.models import Class, Quiz, Question

# Create your models here.
class Profile(models.Model):                          #User Profile  -> Need to create a signal to generate a profile when a user is created.
    email = models.OneToOneField(CustomUser, to_field ="email", on_delete=models.CASCADE)
    name = models.CharField(default='New User',max_length=20)
    roll_number = models.IntegerField(default=0)        
 
    class Meta:
        unique_together = (("email", "roll_number"))
    
    def __str__(self):
        return self.name

class Result(models.Model):
    email = models.ForeignKey(CustomUser, to_field="email", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)    #Unique quiz question
    answer = models.TextField(max_length=200)   #Answer to the question
    score = models.IntegerField()       #Score for current question

