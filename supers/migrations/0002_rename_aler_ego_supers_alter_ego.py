# Generated by Django 4.0.3 on 2022-03-17 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supers',
            old_name='aler_ego',
            new_name='alter_ego',
        ),
    ]
