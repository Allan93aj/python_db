# Generated by Django 5.0.3 on 2024-04-04 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(verbose_name=255)),
                ('email', models.TextField(verbose_name=255)),
                ('setor', models.TextField(verbose_name=255)),
            ],
        ),
    ]
