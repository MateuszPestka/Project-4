# Generated by Django 3.2.16 on 2022-12-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20221208_0225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='special_requirements',
            field=models.TextField(blank=True),
        ),
    ]
