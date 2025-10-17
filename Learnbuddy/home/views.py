from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact, CSKnowledgeArea, CSLearningPath, Hackathon, ITProfile
from .forms import ContactForm, MessageForm, ITProfileForm
from django.http import JsonResponse
import json
import os
import requests
from django.conf import settings

def home(request):
    hackathons = Hackathon.objects.all().order_by('-start_date')[:3]
    return render(request, 'home.html', {'hackathons': hackathons})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            desc = form.cleaned_data['desc']
            contact = Contact(name=name, email=email, desc=desc)
            contact.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def learning_advisor(request):
    learning_paths = CSLearningPath.objects.all()
    return render(request, 'learning_advisor.html', {'learning_paths': learning_paths})

def learning_path_detail(request, path_id):
    learning_path = CSLearningPath.objects.get(id=path_id)
    knowledge_areas = CSKnowledgeArea.objects.filter(learning_path=learning_path)
    return render(request, 'learning_path_detail.html', {
        'learning_path': learning_path,
        'knowledge_areas': knowledge_areas
    })

def chat_with_ai(message):
    # Using Groq API as free alternative
    api_key = settings.GROQ_API_KEY if hasattr(settings, 'GROQ_API_KEY') else settings.OPENAI_API_KEY
    
    # Try multiple models in case some are unavailable
    models_to_try = [
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768",
        "llama3-8b-8192",
        "gemma2-9b-it"
    ]
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    for model in models_to_try:
        try:
            data = {
                "messages": [
                    {"role": "system", "content": "You are a helpful computer science learning assistant. Provide clear, concise explanations and examples to help students understand concepts. When appropriate, include practice questions to test understanding."},
                    {"role": "user", "content": message}
                ],
                "model": model,
                "max_tokens": 1000
            }
            
            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            elif response.status_code == 400 and "model" in response.text.lower():
                # Model not available, try next one
                continue
            else:
                return f"Error: {response.status_code} - {response.text}"
                
        except Exception as e:
            continue
    
    return "Error: Unable to connect to any available AI models. Please check your API key or try again later."

def generate(request):
    result = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            result = chat_with_ai(message)
    else:
        form = MessageForm()
    return render(request, 'generate.html', {'form': form, 'result': result})

def it_profiles(request):
    result = None
    if request.method == 'POST':
        form = ITProfileForm(request.POST)
        if form.is_valid():
            profile = form.cleaned_data['profile']
            question = form.cleaned_data.get('question', '')
            
            profile_info = {
                'software_developer': 'Software Developer',
                'data_scientist': 'Data Scientist',
                'cybersecurity_analyst': 'Cybersecurity Analyst',
                'cloud_engineer': 'Cloud Engineer',
                'devops_engineer': 'DevOps Engineer',
                'network_administrator': 'Network Administrator',
                'ui_ux_designer': 'UI/UX Designer',
                'database_administrator': 'Database Administrator',
                'ai_engineer': 'AI Engineer',
                'product_manager': 'IT Product Manager'
            }
            
            profile_name = profile_info.get(profile, profile)
            
            if question:
                prompt = f"Tell me about the {profile_name} role and answer this specific question: {question}"
            else:
                prompt = f"Provide detailed information about the {profile_name} IT career path including: required skills, education, daily responsibilities, career progression, average salary range, job outlook, and recommended resources for learning."
            
            result = chat_with_ai(prompt)
    else:
        form = ITProfileForm()
    
    return render(request, 'it_profiles.html', {'form': form, 'result': result})

def hackathons(request):
    # hackathons = Hackathon.objects.all().order_by('start_date')
    return render(request, 'hackathons.html', {'hackathons': hackathons})
