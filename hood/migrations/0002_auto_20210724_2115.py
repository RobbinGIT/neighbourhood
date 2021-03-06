# Generated by Django 3.1.3 on 2021-07-24 18:15

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='hood_description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNo', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('profile_pic', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
