from django import forms

class Information(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100,widget=forms.PasswordInput)



class SignUpForm(forms.Form):
	first_name = forms.CharField(label='Your first name', max_length=100)
	last_name = forms.CharField(label='Your last name', max_length=100)
	email = forms.CharField(label='Your email', max_length=100)
	username = forms.CharField(label='Your username', max_length=100)
	password = forms.CharField(label='Your password', max_length=100)
	age = forms.CharField(label='Your age', max_length=100)
	work_experience= forms.CharField(label='Your work experience', max_length=100)
