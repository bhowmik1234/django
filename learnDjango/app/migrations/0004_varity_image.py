# Generated by Django 4.1 on 2024-08-10 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_review_collage_cetificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='varity',
            name='image',
            field=models.ImageField(default='', upload_to='assests/'),
        ),
    ]
