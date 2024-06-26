# Generated by Django 4.2.6 on 2024-03-23 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('jobTitle', models.CharField(max_length=100)),
                ('select', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('useremail', models.EmailField(max_length=254)),
                ('busines_email', models.EmailField(max_length=254)),
                ('userphno', models.CharField(max_length=20)),
                ('userjob', models.CharField(max_length=150)),
                ('userCompany', models.CharField(max_length=160)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SignInUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('re_password', models.CharField(max_length=100)),
            ],
        ),
    ]
