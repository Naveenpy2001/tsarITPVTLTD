# Generated by Django 4.2.6 on 2024-04-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_userregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='terms_of_use_agreed',
            field=models.BooleanField(default=False),
        ),
    ]
