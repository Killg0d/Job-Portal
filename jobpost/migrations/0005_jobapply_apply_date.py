# Generated by Django 4.2 on 2023-05-23 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0004_jobapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapply',
            name='apply_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
