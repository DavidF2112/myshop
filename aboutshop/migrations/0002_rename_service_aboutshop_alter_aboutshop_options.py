# Generated by Django 5.0.1 on 2024-09-20 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Aboutshop',
        ),
        migrations.AlterModelOptions(
            name='aboutshop',
            options={'ordering': ('name',), 'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
    ]
