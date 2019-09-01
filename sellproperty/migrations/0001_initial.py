# Generated by Django 2.2.4 on 2019-09-01 07:41

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import sellproperty.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='sellproperty.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SellProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('full_description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('key_features', ckeditor.fields.RichTextField()),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
                ('status', models.CharField(choices=[('draf', 'Draft'), ('published', 'Published')], default='published', max_length=12)),
                ('location', models.CharField(max_length=200)),
                ('google_map', models.URLField()),
                ('main_image', models.ImageField(default='default.jpg', upload_to=sellproperty.models.upload_image_path)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to=sellproperty.models.upload_image_path)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to=sellproperty.models.upload_image_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sellproperty.Category')),
                ('realator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(default='banglo', on_delete=django.db.models.deletion.DO_NOTHING, to='sellproperty.Type')),
            ],
            options={
                'ordering': ['-created'],
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]