# Generated by Django 2.2.7 on 2020-01-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameLibrary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.CharField(default='Game description', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
