# Generated by Django 4.0.3 on 2022-03-26 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admpage', '0008_worker_sdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='category',
        ),
    ]
