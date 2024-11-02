from django import forms
class UserRegister(forms.Form):
    # username = forms.CharField(label='Введите логин', max_length=60)
    # password = forms.CharField(widget=forms.PasswordInput, label='Введите пароль')           # возможны варианты
    # repeat_password = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    # age = forms.DecimalField(label='Введите свой возраст', max_digits=3)                     # возможны варианты


    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")
    age = forms.IntegerField(min_value=0, max_value=200, label="Введите свой возраст")