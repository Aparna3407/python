# Generated by Django 5.0 on 2024-01-02 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-07-21'),
            preserve_default=False,
        ),
    ]