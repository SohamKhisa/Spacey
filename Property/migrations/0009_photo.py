# Generated by Django 4.0.2 on 2022-02-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0008_business_facilities_climatecontrolled_facilities_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
            ],
        ),
    ]
