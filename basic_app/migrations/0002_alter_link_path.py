# Generated by Django 4.1.4 on 2022-12-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='path',
            field=models.FilePathField(),
        ),
    ]
