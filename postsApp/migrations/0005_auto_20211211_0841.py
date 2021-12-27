# Generated by Django 3.2.9 on 2021-12-11 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0004_alter_post_postedon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='post',
            name='logo',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentedOn', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=200, null=True)),
                ('msg', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(null=True, upload_to='media')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postsApp.post')),
            ],
        ),
    ]