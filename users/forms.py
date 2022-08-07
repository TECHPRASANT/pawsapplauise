""" 
    Author: Prashant Bhandari
    Project Name: PawsApplause
    Purpose: This file contains the forms for the users.
    Date: 8/6/2022

"""

from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, )
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True )
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].label = ""
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control',
            'type': 'text',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })
        self.fields['first_name'].label = ""
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
            'class': 'form-control',
            'type': 'text',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })
        self.fields['last_name'].label = ""
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
            'class': 'form-control',
            'type': 'text',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })
   
        self.fields['email'].label = ""
        self.fields['email'].widget.attrs.update({
            'placeholder' : 'Email',
            'class': 'form-control',
            'type': 'email',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })
        self.fields['password1'].label = ""
        self.fields['password1'].widget.attrs.update({
            'placeholder' : 'Password',
            'class': 'form-control',
            'type': 'password',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })
        self.fields['password2'].label = ""
        self.fields['password2'].widget.attrs.update({
            'placeholder' : 'Confirm Password',
            'class': 'form-control',
            'type': 'password',
            'required': True,
            'autofocus': True,
            'autocomplete': 'off'
        })



            
class ResetForm(PasswordResetForm):
    email = forms.EmailField()    
    fields = ['email']
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        self.fields['email'].label=""
      
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-control', 
            'required':'', 
            'type':'email', 
            'placeholder':'Email',
            }) 




