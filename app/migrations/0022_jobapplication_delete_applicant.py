# Generated by Django 4.2.6 on 2024-04-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_applicant_delete_userregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('resume', models.FileField(upload_to='resumes/')),
                ('country_code', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('aadhar_card', models.CharField(max_length=20)),
                ('fresher', models.BooleanField(default=False)),
                ('applied_before', models.BooleanField(default=False)),
                ('prev_employee_id', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Applicant',
        ),
    ]
