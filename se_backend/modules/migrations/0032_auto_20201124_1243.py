# Generated by Django 3.1.3 on 2020-11-24 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0031_question_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.AddField(
            model_name='question',
            name='subtopic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='modules.subtopics'),
        ),
    ]
