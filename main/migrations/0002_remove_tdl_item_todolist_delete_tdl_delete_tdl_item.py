# Generated by Django 4.0.4 on 2022-05-10 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdl_item',
            name='todolist',
        ),
        migrations.DeleteModel(
            name='TDL',
        ),
        migrations.DeleteModel(
            name='TDL_Item',
        ),
    ]
