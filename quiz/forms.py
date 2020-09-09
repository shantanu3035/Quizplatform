
from django import forms
from django.forms import formset_factory, modelformset_factory
from .models import Question, Choice, Quiz

QuestionModelFormset = modelformset_factory(
    Question,
    fields =('question_text','class_number','subject','correct_answer_text'),
    extra=1,
)

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(
        label = 'Option Text',
    )
ChoiceFormset = formset_factory(ChoiceForm, extra=4)

QuizModelFormset = modelformset_factory(        #Get all questions of a particular class (remove this formset)
    Quiz,
    fields = ('question','marks'),
    extra = 4
)


class QuizInfo(forms.Form):
    quiz_id = forms.IntegerField(       #Let this field act as password ? 
        label = "Add a unique ID to this quiz"
    )
    quizdescription = forms.CharField(max_length=20)
    class_number = forms.IntegerField(max_value=12)
    time_limit = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

"""
class QuizInfoMode(forms.Form):
    class Meta:
        model = Quiz
        fields = ['quiz_id''quizdescription','class_number']

"""

class AnswerChoiceForm(forms.Form):
    choices = forms.ModelChoiceField(queryset=None, widget=forms.RadioSelect,empty_label=None)

    def __init__(self, qid, *args, **kwargs):
        super(AnswerChoiceForm, self).__init__(*args, **kwargs)
        self.fields['choices'].choices = Choice.objects.filter(question=qid)

AnswerFormset = formset_factory(AnswerChoiceForm, extra=0)    #Not Needed.



