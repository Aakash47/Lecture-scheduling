from django import forms
from .models import Lecture, Course, Instructor
from django.contrib.auth.models import User

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['course', 'instructor', 'date']
    
        widgets = {'date': forms.DateInput(attrs={'type':'date'}),}

        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class InstructorRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )
        instructor = Instructor.objects.create(
            user=user,
            name=self.cleaned_data['name']
        )
        return instructor

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'level', 'description', 'image']
