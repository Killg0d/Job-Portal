# Generated by Django 4.2 on 2023-05-23 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_jobprovider_company'),
        ('jobpost', '0003_alter_job_end_date_alter_job_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpost.job')),
                ('job_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobprovider')),
                ('job_seeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.jobseeker')),
            ],
            options={
                'unique_together': {('job_seeker', 'job')},
            },
        ),
    ]
