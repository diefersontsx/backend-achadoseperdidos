# Generated by Django 3.2.7 on 2021-09-15 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_objeto_imagem_objeto'),
    ]

    operations = [
        migrations.AddField(
            model_name='objeto',
            name='dono_cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='objeto',
            name='dono_nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]