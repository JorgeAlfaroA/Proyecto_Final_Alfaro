# Generated by Django 4.2.6 on 2023-11-08 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('subtitulo', models.CharField(max_length=50)),
                ('texto', models.TextField(max_length=2000)),
                ('autor', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes_posts')),
                ('fecha', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
