# Generated by Django 5.1.4 on 2025-01-01 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_question_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
