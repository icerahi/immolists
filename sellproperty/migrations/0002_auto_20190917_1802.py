# Generated by Django 2.2.3 on 2019-09-17 18:02

from django.db import migrations
import places.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sellproperty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellproperty',
            name='property_location',
            field=places.fields.PlacesField(blank=True, max_length=255, null=True),
        ),
    ]
