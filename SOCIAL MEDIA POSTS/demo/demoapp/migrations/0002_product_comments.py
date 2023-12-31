# Generated by Django 4.2.4 on 2023-11-19 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_cmt', models.DateTimeField(auto_now_add=True, null=True)),
                ('name_cmt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to='demoapp.product')),
            ],
        ),
    ]
