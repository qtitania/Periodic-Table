# Generated by Django 3.2.14 on 2022-07-23 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]