# Generated by Django 4.2 on 2023-05-27 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0006_alter_job_options_alter_job_table_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='jobapply',
            options={'verbose_name': 'Application', 'verbose_name_plural': 'Applications'},
        ),
    ]
