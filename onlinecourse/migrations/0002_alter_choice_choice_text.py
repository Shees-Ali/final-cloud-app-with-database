# Generated by Django 4.2.3 on 2023-07-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(choices=[], max_length=200),
        ),
    ]
