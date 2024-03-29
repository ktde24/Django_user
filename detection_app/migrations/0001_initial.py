# Generated by Django 5.0 on 2024-01-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bounding_box_origin_x', models.FloatField()),
                ('bounding_box_origin_y', models.FloatField()),
                ('bounding_box_width', models.FloatField()),
                ('bounding_box_height', models.FloatField()),
                ('categories_index', models.IntegerField()),
                ('categories_score', models.FloatField()),
                ('categories_display', models.CharField(max_length=255)),
                ('categories_category_name', models.CharField(max_length=255)),
            ],
        ),
    ]
