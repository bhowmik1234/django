# Generated by Django 4.1 on 2024-08-09 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='varity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('image', models.ImageField(upload_to='assests/')),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
