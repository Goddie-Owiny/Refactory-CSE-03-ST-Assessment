# Generated by Django 5.0.4 on 2024-05-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='entry_scheme',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='intake',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='sponsorship',
            field=models.CharField(max_length=50),
        ),
    ]
