# Generated by Django 2.2.19 on 2022-03-17 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
        ('mailing', '0003_auto_20220317_2049'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Consumer',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='customer',
            new_name='consumer',
        ),
    ]
