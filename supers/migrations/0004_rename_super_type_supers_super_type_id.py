# Generated by Django 4.0.3 on 2022-03-21 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0003_alter_supers_super_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supers',
            old_name='super_type',
            new_name='super_type_id',
        ),
    ]
