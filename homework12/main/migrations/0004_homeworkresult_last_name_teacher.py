# Generated by Django 3.2.1 on 2021-10-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_homeworkresult_data_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworkresult',
            name='last_name_teacher',
            field=models.CharField(max_length=50,
                                   null=True,
                                   verbose_name='Last Teacher name'),
        ),
    ]
