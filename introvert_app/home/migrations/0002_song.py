# Generated by Django 3.2.7 on 2021-10-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('artist', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='')),
                ('audio_link', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
    ]
