# Generated by Django 2.0 on 2019-05-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_name', models.CharField(max_length=25)),
                ('biz_category', models.CharField(max_length=25)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
    ]
