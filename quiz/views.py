from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Quiz, Choice, Class
from profiles.models import Result
from users.models import CustomUser
from .forms import QuestionModelFormset, ChoiceFormset, QuizModelFormset, QuizInfo, AnswerFormset, AnswerChoiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from collections import Counter

@login_required
def homepage(request):                                       #Common Homepage for all 
    questions = Question.objects.all()
    context = {
        "questions":questions
    }
    return render(request, 'quiz/home.html', context)

class QuestionListView(ListView):                            #Shows List of all questions - QuestionBank (Add Pagination and sorting functionality)
    model = Question
    template_name = 'quiz/home.html'                         #Looks for template at :	<app_name>/<model>_<view_type>.html 
    context_object_name = 'questions'                        #By default it will be object
    ordering = ['-pub_date']                                 #- sign for reverse on field name

    def get_queryset(self):
        return ()
        
class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/dashboard.html'
    context_object_name = 'quizes'
    ordeting = ['pub_date']

    def get_queryset(self):
        q = (Quiz.objects.values('quiz_id','class_number','quizdescription').distinct())
        return (q)


class QuestionDetailView(DetailView):       #Get list of questions based on class
    model = Question
    template_name = 'quiz/home.html'
    context_object_name = 'questions'
    ordering = ['-pub_date']

    def get_queryset(self):                                  
        class_number = self.kwargs.get("class_number")
        return Question.objects.all().filter(class_number=class_number)

class QuizDetailView(DetailView):
    model = Quiz
    template_name = 'quiz/dashboard.html'
    context_object_name = 'quizes'

    def get_queryset(self):             #Get List of all quiz based on quiz description
        class_number = self.kwargs.get("quizdescription") 
        return Quiz.objects.all().filter(quizdescription=quizdescription)

@login_required
def quizattempt(request, email, quiz_id):        #this method handles the quiz form POST request, calculates the results and saves it in database.
    return None



"""
Create views for:
1. Creating a question (Done)
2. Creating a new Quiz.
3. Attempting a quiz.
"""

@login_required         #Allows user to create questions and add corresponding choices for that question -> Have to add + Functionality
def createQuestion(request):
    if request.user.user_type == 'TE':
        template_name = 'quiz/question_form.html'
        heading_message = 'Add Questions'
        if request.method == 'POST':
            qformset = QuestionModelFormset(request.POST)
            cformset = ChoiceFormset(request.POST)
            if qformset.is_valid():
                for form in qformset:
                    question_text = form.cleaned_data.get('question_text')
                    class_number = form.cleaned_data.get('class_number')
                    subject = form.cleaned_data.get('subject')
                    correct_answer = form.cleaned_data.get('correct_answer_text')
                    if question_text and class_number and subject and correct_answer:
                        question_pk = form.save() #Primary key of question -> useful for choice form
                        if cformset.is_valid():
                            for cform in cformset:
                                choice_text = cform.cleaned_data.get('choice_text')
                                if choice_text:
                                    Choice(question=question_pk, choice_text=choice_text).save()  
                return redirect('home')
        elif request.method == 'GET':
            qformset = QuestionModelFormset(queryset=Question.objects.none()) #Dont display already saved questions
            cformset = ChoiceFormset(request.GET or None)
        return render(request, template_name, {
            'formset':qformset,
            'cformset':cformset,
            'heading':heading_message
        })

#This method allows users to plug questions in a quiz and then save the quiz. -> Password ??
#Quiz ID should be generated first time a question is added, and it should remain the same for all subsequent questions**
#Questions should be filtered on the basis of the class for which the quiz is meant for
#For every question -> author must allocate the marks for this quiz.
#Author will be the current user who is logged in 
#Quiz description needs to be set just once.

@login_required
def createQuiz(request): 
    if request.user.user_type == 'TE':
        template_name = "quiz/quiz_form.html"
        heading_message = "Create Quiz"
        if request.method == "GET":
            quizformset = QuizModelFormset(queryset=Quiz.objects.none()) #Query set
            quizinfo = QuizInfo(request.GET or None)
        elif request.method == "POST":
            quizformset = QuizModelFormset(request.POST)
            quizinfo = QuizInfo(request.POST)
            if quizinfo.is_valid():         #One time info is valid
                quiz_id = quizinfo.cleaned_data.get("quiz_id")
                quizdescription = quizinfo.cleaned_data.get("quizdescription")
                class_number = quizinfo.cleaned_data.get("class_number")
                time_limit = quizinfo.cleaned_data.get("time_limit")        #Need to add this field in database for attempt check
                if quizformset.is_valid():
                    for form in quizformset:
                        question = form.cleaned_data.get("question")
                        marks = form.cleaned_data.get("marks")
                        if question and marks:
                            Quiz(quiz_id=quiz_id,author=request.user,class_number=Class.objects.all().get(class_number=class_number),question=question,marks=marks,quizdescription=quizdescription).save()
                    return redirect('home')
        return render(request, template_name, {
            'quizformset':quizformset,
            'quizinfo':quizinfo
        }
        )


"""
This method allows students to attempt a quiz defined by a QUIZ_ID. 
For every question in quiz_id:
    Get the 4 choices from the Choices Table
    Display the 4 choices as a form : Only 1 option can be selected
    For every question: Answers should be saved in the Results table [ ]


"""

@login_required         
def attemptquiz(request, quiz_id):
    if request.user.user_type == 'ST':
        template_name = "quiz/quiz_attempt.html"
        questions = Quiz.objects.filter(quiz_id=quiz_id)
        if request.method == 'GET':
            answerforms = {}
            for question in questions:
                answerchoiceform = AnswerChoiceForm(qid=question.question.id)
                answerformset = AnswerFormset(form_kwargs={'qid':question.question.id})
                answerforms[question.question.id] = answerchoiceform
        elif request.method == 'POST':
            for question in questions:
                answerformset = AnswerFormset(request.POST,form_kwargs={'qid':question.question.id})
                for form in answerformset: 
                    if answerformset.is_valid():
                        answer = form.cleaned_data.get("choices").choice_text
                        correct_answer = Question.objects.values("correct_answer_text").get(id=question.question.id)
                        if answer.upper() == correct_answer['correct_answer_text'].upper():
                            score = Quiz.objects.values("marks").get(question=question.question.id)['marks']
                        else:
                            score = 0
                        email = request.user
                        quiz = question
                        Result(email=email,quiz=quiz,answer=answer,score=score).save()
            return redirect('home')
        return render(request, template_name, {
            'questions':questions,
            'answerformset':answerformset,
            'answerforms':answerforms,
            'answerchoiceform':answerchoiceform
        })


    
    