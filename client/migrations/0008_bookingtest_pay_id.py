# Generated by Django 4.0.2 on 2022-03-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_bookingtest_pay_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingtest',
            name='pay_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
