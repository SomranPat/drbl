# Generated by Django 4.0.3 on 2022-04-26 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admpage', '0004_alter_attendance_atim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grievance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_title', models.CharField(max_length=100, null=True)),
                ('g_details', models.CharField(max_length=500, null=True)),
                ('g_status', models.CharField(choices=[('Active', 'Active'), ('Unactive', 'Unactive'), ('Finished', 'Finished')], max_length=20, null=True)),
                ('g_date', models.DateField(auto_now_add=True, null=True)),
                ('worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admpage.worker')),
            ],
        ),
    ]
