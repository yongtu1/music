# Generated by Django 2.1.8 on 2019-06-01 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='board_num',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
