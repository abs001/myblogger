# Generated by Django 3.1.5 on 2021-01-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_description', models.TextField()),
                ('blog_image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('site_address', models.TextField()),
                ('site_logo', models.ImageField(upload_to='')),
                ('social_fb', models.CharField(max_length=200)),
                ('social_li', models.CharField(max_length=200)),
                ('social_tw', models.CharField(max_length=200)),
            ],
        ),
    ]
