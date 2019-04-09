from django.contrib.auth.forms import UserCreationForm
from registration_app.models import Myuser
from django import forms



class Registration_form(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    class Meta:
        model = Myuser
        fields = ('email','password1','password2')
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords Don't Match")
        return password2

    def save(self, commit= True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user













    # email = forms.CharField(label='Email', widget=forms.EmailInput)
    # # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # # password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
    #
    # class Meta(UserCreationForm.Meta):
    #     model = Myuser
    #     fields =('email','password1','password2')
    #
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
