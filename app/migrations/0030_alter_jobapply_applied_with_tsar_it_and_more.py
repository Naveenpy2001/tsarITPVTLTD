# Generated by Django 4.2.6 on 2024-06-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_jobapply_application_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapply',
            name='applied_with_tsar_it',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='is_fresher',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='terms_of_use_agreed',
            field=models.CharField(max_length=200, null=True),
        ),
    ]