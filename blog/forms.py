from django.forms import ModelForm
from .models import Comment
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
        