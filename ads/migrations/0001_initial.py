# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 13:44
from __future__ import unicode_literals

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('name', models.CharField(max_length=140)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(upload_to=b'')),
                ('aboutUs', models.TextField()),
                ('ranking', models.PositiveIntegerField(default=0)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Category')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
            ],
        ),
        migrations.CreateModel(
            name='DetPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('finishDate', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('alt', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='LinksCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Link')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('mounthPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('yearPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('numberImage', models.PositiveSmallIntegerField()),
                ('numberPhone', models.PositiveSmallIntegerField()),
                ('type_ad', models.CharField(choices=[('BASICO', 'Basico'), ('FINDME', 'FindMe'), ('STARTUP', 'StartUp')], default='BASICO', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='detplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Plan'),
        ),
        migrations.AddField(
            model_name='detplan',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companytags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Tag'),
        ),
        migrations.AddField(
            model_name='company',
            name='links',
            field=models.ManyToManyField(through='ads.LinksCompany', to='ads.Link'),
        ),
        migrations.AddField(
            model_name='company',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.Plan'),
        ),
        migrations.AddField(
            model_name='company',
            name='tags',
            field=models.ManyToManyField(through='ads.CompanyTags', to='ads.Tag'),
        ),
    ]
