# Generated by Django 4.0.2 on 2022-02-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pic',
            field=models.FileField(default='avtar.png', upload_to='Profile Pic'),
        ),
    ]