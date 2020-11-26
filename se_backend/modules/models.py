from django.db import models
import uuid
# from crum import get_current_user  
import crum      
# As model field:
from django.contrib.auth import get_user_model as user_model
User = user_model()

# Create your models here.
class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name=models.CharField(max_length=200)
    description=models.TextField()
    status=models.CharField(max_length=200,default="Created",editable=False)
    time_created=models.DateTimeField(auto_now_add=True)
    userid = models.CharField(max_length=45,null=False, blank=True, editable=False, default=crum.get_current_user())

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        userid = crum.get_current_user()
        self.userid = userid.id
        super(Project, self).save(*args, **kwargs)

class Module(models.Model):
    module_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module_logo = models.ImageField(upload_to='module_logo')
    module_number = models.IntegerField()
    module_name = models.CharField(max_length=200)
    status=models.CharField(max_length=200,default="Created",editable=False)
    time_created = models.DateTimeField(auto_now_add=True)
    module_description = models.TextField(max_length=200,null=True,default="description")
    userid = models.CharField(max_length=45,null=False, blank=True, editable=False, default=crum.get_current_user())

    def __str__(self):
        return self.module_name

    def save(self, *args, **kwargs):
        userid = crum.get_current_user()
        self.userid = userid.id
        super(Module, self).save(*args, **kwargs)

class Topics(models.Model):
    topic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    topic_name = models.CharField(max_length=200)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL,null=True)
    topic_number = models.IntegerField()
    topic_description = models.TextField(max_length=400)

    def __str__(self):
        return self.topic_name

class SubTopics(models.Model):
    subtopic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subtopic_name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topics,on_delete=models.SET_NULL,null=True)
    subtopic_number = models.IntegerField()
    subtopic_description = models.TextField(max_length=400)

    def __str__(self):
        return self.subtopic_name

class Content(models.Model):
    content_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subtopic = models.ForeignKey(SubTopics,on_delete=models.SET_NULL,null=True)
    content_number = models.IntegerField()
    title_text = models.CharField(max_length=400)
    title_intro = models.TextField(max_length=4400)
    content_section = models.TextField(max_length=4400)
    media_section = models.CharField(max_length=400)

    def __str__(self):
        return self.title_text

class Question(models.Model):
    question_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey(Module,on_delete=models.SET_NULL,null=True)
    question_number=models.IntegerField()
    subtopic = models.ForeignKey(SubTopics,on_delete=models.SET_NULL,null=True)
    question = models.JSONField(max_length=200,null=True, blank=True)
    question_type = models.IntegerField() #one will indicate open-ended, 2 will indicate multiple choice
    question_status=models.CharField(max_length=200,default="Created",editable=False)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    answer_string = models.JSONField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    userid = models.CharField(max_length=45,null=False, blank=True, editable=False, default=crum.get_current_user())

    def save(self, *args, **kwargs):
        userid = crum.get_current_user()
        self.userid = userid.id
        super(Answer, self).save(*args, **kwargs)