from .models import Comment
from django.contrib.auth.models import User

from django import forms




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['username', 'comment']
        labels = {
            'username':'User Name',
            'comment':'Leave a comment'
        }
        error_messages = {
            'username':
            {'required':'Username must not be empty!'},
            'comment':
            {'required':'Comment must not be empty!'}

           
        }
        

class LoginForm(forms.Form):
    username= forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        labels = {
            'username':'Username',
            'email':'Email',
            'password':'Password'
        }
        error_messages = {
            'username':
            {'required':'Username must not be empty!'},
            'email':
            {'required':'Email must not be empty!'},
            'password':{'required':'Password must not be empty!'}

           
        }