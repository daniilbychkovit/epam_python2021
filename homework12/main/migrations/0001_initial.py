# Generated by Django 3.2.1 on 2021-10-24 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text homework')),
                ('deadline', models.IntegerField(verbose_name='Deadline homework')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, verbose_name='Text homework')),
                ('last_name_student', models.CharField(max_length=50, null=True, verbose_name='Last Student name')),
                ('solution', models.TextField(verbose_name='Homework solution')),
            ],
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='First Human name')),
                ('surname', models.CharField(max_length=50, null=True, verbose_name='Last Human name')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_student', models.CharField(max_length=50, null=True, verbose_name='First Student name')),
                ('last_name_student', models.CharField(max_length=50, null=True, verbose_name='Last Student name')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_teacher', models.CharField(max_length=50, null=True, verbose_name='First Teacher name')),
                ('last_name_teacher', models.CharField(max_length=50, null=True, verbose_name='Last Teacher name')),
            ],
        ),
    ]