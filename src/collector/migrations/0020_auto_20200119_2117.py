# Generated by Django 3.0.2 on 2020-01-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0019_puzzlepiece_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzlepiece',
            name='image_url',
            field=models.CharField(default=None, max_length=256, verbose_name='url of the image if found'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puzzlepiece',
            name='no_image_url_found',
            field=models.NullBooleanField(verbose_name='image url was not found'),
        ),
    ]