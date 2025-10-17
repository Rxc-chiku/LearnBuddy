from django.db import models
from django.contrib.auth.models import User

class ITProfile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skills_required = models.TextField()
    career_path = models.TextField()
    average_salary = models.CharField(max_length=100)
    job_outlook = models.TextField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class CSKnowledgeArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class CSLearningPath(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty_level = models.CharField(max_length=20, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    
    def __str__(self):
        return self.title

class PathAreaRelationship(models.Model):
    path = models.ForeignKey(CSLearningPath, on_delete=models.CASCADE)
    area = models.ForeignKey(CSKnowledgeArea, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

class Hackathon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    organizer = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    registration_url = models.URLField()
    image = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    learning_path = models.ForeignKey(CSLearningPath, on_delete=models.CASCADE)
    knowledge_area = models.ForeignKey(CSKnowledgeArea, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ['user', 'learning_path', 'knowledge_area']
