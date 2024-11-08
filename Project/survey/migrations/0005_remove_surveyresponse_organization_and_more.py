# Generated by Django 5.1.3 on 2024-11-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_alter_surveyresponse_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='q19',
        ),
        migrations.RemoveField(
            model_name='surveyresponse',
            name='q20',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='q8',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='gender',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='occupation',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='platform',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='q16',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='relationship',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='social_media',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='surveyresponse',
            name='time_on_social_media',
            field=models.CharField(max_length=1),
        ),
    ]