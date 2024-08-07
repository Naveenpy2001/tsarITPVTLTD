# Generated by Django 4.2.6 on 2024-06-10 11:01

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_contactmessage_form_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='application_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='aadhar_card_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=12, validators=[django.core.validators.MinLengthValidator(12)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='applied_with_tsar_it',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='country_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='first_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='is_fresher',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='last_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='password',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=15, validators=[django.core.validators.MinLengthValidator(10)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='previous_employee_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='jobapply',
            name='terms_of_use_agreed',
            field=models.BooleanField(default=False),
        ),
    ]
