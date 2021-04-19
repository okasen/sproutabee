from django.contrib.auth.forms import get_user_model, UserCreationForm, UserChangeForm
from .models import User
from django import forms
from django.forms import ModelForm

user = get_user_model()

class CustomUserCreationForm(ModelForm):
    password1 = forms.CharField(label='create a password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='type that password again', widget=forms.PasswordInput)

    #TO DO: Ensure that users signing up are at least 13

    class Meta:
        model = user
        fields = ('email', 'username', 'date_of_birth')


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(ModelForm):

    class Meta:
        model = user
        fields = ('email', 'username', 'date_of_birth', 'is_staff')

    def clean_passsword2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2
