# Generated by Django 4.0.2 on 2022-03-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='verify',
            field=models.BooleanField(default=False),
        ),
    ]
