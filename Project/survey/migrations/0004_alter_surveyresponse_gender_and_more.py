# Generated by Django 5.1.3 on 2024-11-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_surveyresponse_delete_survey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='occupation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='organization',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='relationship',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='social_media',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='time_on_social_media',
            field=models.CharField(max_length=100),
        ),
    ]
