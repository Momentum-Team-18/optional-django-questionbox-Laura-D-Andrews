# Generated by Django 3.1.12 on 2023-05-26 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
