# Generated by Django 4.0.3 on 2022-03-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flipcoin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
