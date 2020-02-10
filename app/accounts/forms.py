from django import forms
from django.contrib.auth.models import User


class ResetPassword(forms.Form):
    password1 = forms.CharField(label='New Password', min_length=8, max_length=100, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Retype Password', min_length=8, max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    "The two password is not the same"
                )
            elif password1.isalpha():
                raise forms.ValidationError(
                    "You also need number for password"
                )
            elif password1.isdigit():
                raise forms.ValidationError(
                    "You also need char for password"
                )
