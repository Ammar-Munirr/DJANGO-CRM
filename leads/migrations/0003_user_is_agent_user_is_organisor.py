# Generated by Django 4.2.2 on 2023-08-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_userprofile_agent_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=True),
        ),
    ]
