# Generated by Django 4.2.4 on 2023-11-19 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_comments',
            old_name='product_name',
            new_name='post',
        ),
    ]
