# Generated by Django 4.2.4 on 2023-12-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='mail',
            field=models.EmailField(default='none@gmail.com', max_length=254),
        ),
    ]