from django.contrib import admin
from .models import Contact, ITProfile, CSKnowledgeArea, CSLearningPath, Hackathon, UserProgress

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email')
    readonly_fields = ('date',)

admin.site.register(ITProfile)
admin.site.register(CSKnowledgeArea)
admin.site.register(CSLearningPath)
admin.site.register(Hackathon)
admin.site.register(UserProgress)
