# Generated by Django 3.2.10 on 2022-02-03 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_replaycomment_replay'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReplayComment',
        ),
    ]
