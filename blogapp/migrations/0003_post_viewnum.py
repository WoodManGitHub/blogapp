# Generated by Django 2.2.1 on 2019-05-11 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_auto_20190511_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='viewnum',
            field=models.PositiveIntegerField(default=0),
        ),
    ]