# Generated by Django 3.2.3 on 2021-05-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_quiz_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='correct_answer',
            field=models.CharField(choices=[('C', 'Correct'), ('N', 'Not Correct')], default='C', max_length=1),
        ),
    ]
