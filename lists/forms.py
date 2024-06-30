from django import forms
from datetime import datetime


class TodolistForm(forms.Form):
    text=forms.CharField(max_length=120, 
                         widget=forms.TextInput(attrs={'class':'inputstyle','type':'text', 'rows': 3, 'placeholder':'Enter a task here'}))
    date=forms.DateField(initial=datetime.now().date, widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    time=forms.TimeField(initial=datetime.now().time, widget=forms.TimeInput(attrs={'class':'form-control', 'type':'time'}))




class ConfirmDeleteForm(forms.Form):
    confirm = forms.BooleanField(label='Confirm deletion', required=True)