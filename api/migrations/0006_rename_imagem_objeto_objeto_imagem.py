# Generated by Django 3.2.7 on 2021-09-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_imagem_local_local_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='objeto',
            old_name='imagem_objeto',
            new_name='imagem',
        ),
    ]
