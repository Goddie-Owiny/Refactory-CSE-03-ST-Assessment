# Generated by Django 5.0.3 on 2024-05-17 09:23

import Ritah.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, validators=[Ritah.models.validate_letters])),
                ('lastname', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
                ('entry_scheme', models.CharField(max_length=255)),
                ('intake', models.IntegerField(max_length=255)),
                ('sponsorhip', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField(max_length=255)),
                ('residence', models.CharField(max_length=255)),
            ],
        ),
    ]
