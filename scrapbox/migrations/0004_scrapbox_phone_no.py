# Generated by Django 4.2.7 on 2023-12-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbox', '0003_remove_posts_liked_by_remove_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapbox',
            name='phone_no',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
