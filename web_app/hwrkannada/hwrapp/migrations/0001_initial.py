# Generated by Django 2.0.4 on 2018-04-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
    ]
