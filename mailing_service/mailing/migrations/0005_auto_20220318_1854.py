# Generated by Django 2.2.19 on 2022-03-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_auto_20220317_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='name',
            field=models.CharField(default='sdfs', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mailing',
            name='title',
            field=models.CharField(default='nooo', max_length=50),
            preserve_default=False,
        ),
    ]
