# Generated by Django 3.2.16 on 2022-12-08 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_special_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='group_size',
            field=models.IntegerField(default=0),
        ),
    ]
