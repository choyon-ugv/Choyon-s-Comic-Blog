# Generated by Django 4.1.6 on 2023-02-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
