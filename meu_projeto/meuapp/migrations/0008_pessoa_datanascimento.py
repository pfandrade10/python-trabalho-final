# Generated by Django 3.2.3 on 2021-06-14 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuapp', '0007_pessoa_telefones'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='dataNascimento',
            field=models.DateField(null=True),
        ),
    ]
