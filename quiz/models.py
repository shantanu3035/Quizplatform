from django.db import models
from django.utils import timezone
from users.models import CustomUser

# Create your models here.

class Class(models.Model):
    class_number = models.IntegerField(primary_key=True)         

    def __str__(self):
        return (str(self.class_number)) 

class Question(models.Model):
    question_text = models.TextField(max_length=200, unique=True)
    class_number = models.ForeignKey(Class, on_delete=models.CASCADE) 
    pub_date = models.DateField('date published', default= timezone.now())
    ENGLISH = 'ENG'
    MATHS = 'MATH'
    SCIENCE = 'SCI'
    SUBJECT_CHOICES = [
        (ENGLISH, 'English'),
        (MATHS, 'Maths'),
        (SCIENCE, 'Science')
    ]
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=4)
    correct_answer_text = models.TextField(max_length=200)

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)

    def __str__(self):
        return self.choice_text

class Quiz(models.Model):       #Multiple primary keys would make this simpler.
    quiz_id = models.IntegerField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1) #If user deleted, then delete Quiz as well
    class_number = models.ForeignKey(Class,on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks = models.IntegerField(default=1)      #Marks for the question in the current quiz
    quizdescription = models.TextField(max_length=20)

    def __str__(self):
        return (self.question.question_text + '-' + str(self.marks))




