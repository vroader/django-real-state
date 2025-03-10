# Generated by Django 3.2.7 on 2025-02-01 21:55

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250, verbose_name='Property Title')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=True, populate_from='title', unique=True)),
                ('ref_code', models.CharField(blank=True, max_length=255, unique=True, verbose_name='Porperty Reference Code')),
                ('description', django_countries.fields.CountryField(default='BR', max_length=2, verbose_name='Country')),
                ('country', django_countries.fields.CountryField(default='BR', max_length=2, verbose_name='Country')),
                ('city', models.CharField(default='Brasilia', max_length=180, verbose_name='City')),
                ('postal_code', models.CharField(default='140', max_length=100, verbose_name='Postal Code')),
                ('street_address', models.CharField(default='Quadra 1', max_length=150, verbose_name='Street Address')),
                ('property_number', models.IntegerField(default=122, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Property Number')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Price')),
                ('tax', models.DecimalField(decimal_places=2, default=0.15, help_text='15% property tax charged', max_digits=6, verbose_name='Property Tax')),
                ('plot_area', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Plot Area m^2')),
                ('total_floors', models.IntegerField(default=0, verbose_name='Number of Floors')),
                ('bedrooms', models.IntegerField(default=1, verbose_name='Bedrooms')),
                ('bathrooms', models.DecimalField(decimal_places=2, default=1.0, max_digits=4, verbose_name='Bathrooms')),
                ('advert_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent'), ('Auction', 'Auction')], default='For Sale', max_length=50, verbose_name='Advert Type')),
                ('property_type', models.CharField(choices=[('House', 'House'), ('Apartment', 'Apartment'), ('Office', 'Office'), ('Warehouse', 'Warehouse'), ('Commercial', 'Commercial'), ('Other', 'Other')], default='Other', max_length=50, verbose_name='Property Type')),
                ('cover_photo', models.ImageField(blank=True, default='/house_sample.jpg', null=True, upload_to='', verbose_name='Main Photo')),
                ('photo1', models.ImageField(blank=True, default='/interior_sample.jpg', null=True, upload_to='', verbose_name='Photo 1')),
                ('photo2', models.ImageField(blank=True, default='/exterior_sample.jpg', null=True, upload_to='', verbose_name='Photo 2')),
                ('photo3', models.ImageField(blank=True, default='/bedroom_sample.jpg', null=True, upload_to='', verbose_name='Photo 3')),
                ('photo4', models.ImageField(blank=True, default='/bathroom_sample.jpg', null=True, upload_to='', verbose_name='Photo 4')),
                ('published_status', models.BooleanField(default=False, verbose_name='Published Status')),
                ('views', models.IntegerField(default=0, verbose_name='Total Views')),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
        migrations.CreateModel(
            name='PropertyViews',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ip', models.CharField(max_length=250, verbose_name='IP Address')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_views', to='properties.property')),
            ],
            options={
                'verbose_name': 'Total Views on property',
                'verbose_name_plural': 'Total property views',
            },
        ),
    ]
