# Generated by Django 4.0.3 on 2022-05-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
