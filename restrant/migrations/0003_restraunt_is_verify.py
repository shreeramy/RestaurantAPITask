# Generated by Django 4.1.3 on 2022-11-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restrant', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]
