# Generated by Django 4.2.4 on 2023-11-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0009_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
