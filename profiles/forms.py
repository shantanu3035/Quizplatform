from django import forms
from users.models import CustomUser
from .models import Profile, Result


#Form for Profile Updation
class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','roll_number']

class TeacherProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name']
