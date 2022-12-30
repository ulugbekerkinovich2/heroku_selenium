# Generated by Django 4.1.4 on 2022-12-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=500)),
                ('path', models.FilePathField(max_length=500)),
            ],
            options={
                'db_table': 'link',
            },
        ),
    ]