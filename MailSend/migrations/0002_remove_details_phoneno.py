# Generated by Django 4.0.4 on 2022-05-21 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MailSend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='PhoneNo',
        ),
    ]