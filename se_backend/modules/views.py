from django.shortcuts import render
# Create your views here.
from rest_framework import status, viewsets

from .models import *
from .serializers import *
from django.views.generic.edit import CreateView
from modules.models import Project

class ProjectCreate(CreateView):
    model = Project
    fields = ['project_name',]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topics.objects.all()
    serializer_class = TopicSerializer

class SubTopicViewSet(viewsets.ModelViewSet):
    queryset = SubTopics.objects.all()
    serializer_class = SubTopicSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
