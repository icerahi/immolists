# Generated by Django 2.2.3 on 2019-09-17 18:09

from django.db import migrations
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sellproperty', '0002_auto_20190917_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellproperty',
            name='property_location',
        ),
        migrations.AddField(
            model_name='sellproperty',
            name='location',
            field=places.fields.PlacesField(blank=True, max_length=255),
        ),
    ]
