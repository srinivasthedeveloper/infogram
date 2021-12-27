# Generated by Django 3.2.9 on 2021-12-06 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0002_auto_20211206_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postedOn',
            field=models.DateField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
