# Generated by Django 2.2.4 on 2019-08-29 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyforsell',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/sellproperty/'),
        ),
    ]
