from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms

# Register your models here.
from .models import *

class ModuleA(admin.ModelAdmin):
    list_display = ('module_name', 'module_number')
    search_fields = ['module_name', 'module_number'] 

class TopicA(admin.ModelAdmin):
    list_display = ('topic_name','topic_number','get_module')
    list_filter = ('module','topic_number')
    search_fields = ['topic_name',] 
    def get_module(self, obj):
        return obj.module.module_name

class SubTopicA(admin.ModelAdmin):
    list_display = ('subtopic_name','subtopic_number','get_topic')
    list_filter = ('topic','subtopic_number')
    def get_topic(self, obj):
        return obj.topic.topic_name

class ContentA(admin.ModelAdmin):
    list_display = ('title_text','get_subtopic')
    list_filter = ('subtopic',)
    def get_subtopic(self, obj):
        return obj.subtopic.subtopic_name

class ProjectA(admin.ModelAdmin):
    list_display = ('project_name', 'description')
    readonly_fields = ('project_name','description',)

    def has_add_permission(self, request):
        return False 
    def has_delete_permission(self, request, obj=None):
        return False  
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(ProjectA, self).changeform_view(request, object_id, extra_context=extra_context)

class AnswersA(admin.ModelAdmin):
    list_display = ('answer_string', 'question', 'project')
    readonly_fields = ('answer_string','project','question')

    def has_add_permission(self, request):
        return False 
    def has_delete_permission(self, request, obj=None):
        return False  
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(AnswersA, self).changeform_view(request, object_id, extra_context=extra_context)

# Register your models here
admin.site.register(Project,ProjectA)
admin.site.register(Module,ModuleA)
admin.site.register(Topics,TopicA)
admin.site.register(SubTopics,SubTopicA)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.unregister(Group)
admin.site.register(Content,ContentA)

admin.site.site_header = "SE Admin Page"
admin.site.index_title = "SE Admin Page"
