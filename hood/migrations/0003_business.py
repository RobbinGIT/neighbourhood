# Generated by Django 3.1.3 on 2021-07-24 18:16

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0002_auto_20210724_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=250)),
                ('business_email', models.CharField(max_length=30)),
                ('business_desc', models.TextField(blank=True)),
                ('business_photo', cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='businessphoto')),
                ('business_hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
