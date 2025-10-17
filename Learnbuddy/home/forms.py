from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    desc = forms.CharField(widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label="Ask your question")
    
class ITProfileForm(forms.Form):
    PROFILE_CHOICES = [
        ('', 'Select an IT profile'),
        ('software_developer', 'Software Developer'),
        ('data_scientist', 'Data Scientist'),
        ('cybersecurity_analyst', 'Cybersecurity Analyst'),
        ('cloud_engineer', 'Cloud Engineer'),
        ('devops_engineer', 'DevOps Engineer'),
        ('network_administrator', 'Network Administrator'),
        ('ui_ux_designer', 'UI/UX Designer'),
        ('database_administrator', 'Database Administrator'),
        ('ai_engineer', 'AI Engineer'),
        ('product_manager', 'IT Product Manager')
    ]
    
    profile = forms.ChoiceField(choices=PROFILE_CHOICES, label="Select an IT Profile")
    question = forms.CharField(widget=forms.Textarea, label="Ask about this IT career", required=False)