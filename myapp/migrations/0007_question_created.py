# Generated by Django 5.1.4 on 2025-01-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_question_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
