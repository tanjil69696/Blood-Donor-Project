# Generated by Django 5.1.6 on 2025-03-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanjilahamed_bloodgroup_app', '0002_alter_blooddonation_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonation',
            name='number',
            field=models.IntegerField(),
        ),
    ]
