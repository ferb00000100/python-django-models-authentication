# Generated by Django 2.2.9 on 2020-10-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201016_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='mainapp.Tag'),
        ),
    ]
