# Generated by Django 4.2.7 on 2023-12-10 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbox', '0004_scrapbox_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address',
            new_name='email',
        ),
    ]