# Generated by Django 4.1.3 on 2022-11-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restrant', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='restraunt',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='restraunt'),
        ),
    ]