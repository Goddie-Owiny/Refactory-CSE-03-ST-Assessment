# Generated by Django 5.0.6 on 2024-05-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6),
        ),
    ]
