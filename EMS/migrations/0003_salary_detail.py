# Generated by Django 2.2.5 on 2021-02-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0002_auto_20210213_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emp_code', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('Number_of_working_days', models.IntegerField()),
                ('Employee_working_days', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
