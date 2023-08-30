from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import CourcesModel
from django import forms

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password Should Be Same'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        label = {'email':'Email'}
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter lastname'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}))


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    class Meta:
        fields = '__all__'
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))

class NoteUploadForm(forms.ModelForm):
    class Meta:
        model = CourcesModel
        fields = ['cname','year','semester','subject','syllabus','note','oldquestion','oldquestionyear','writer','shortdetail']
    writer = forms.CharField(label='Author')
    shortdetail = forms.CharField(widget=forms.Textarea)
    syllabus = forms.FileField(required=False)
    oldquestion = forms.FileField(required=False)
    oldquestionyear = forms.DateField(required=False)



