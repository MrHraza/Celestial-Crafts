# Generated by Django 3.2 on 2024-07-30 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20240728_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]
