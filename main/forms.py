from django import forms
from .models import posts

class addpost(forms.Form):
    add_Title=forms.CharField(label="Title")
    add_Image=forms.ImageField(label="Image")
    add_Content=forms.CharField(label="Content",widget=forms.Textarea)
    model=posts
