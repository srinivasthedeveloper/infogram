# Generated by Django 3.2.9 on 2021-12-22 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0007_auto_20211221_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.TextField(blank=True, max_length=200, null=True)),
                ('field2', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
