# Generated by Django 3.2 on 2021-05-05 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=50)),
                ('identificacion', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField(auto_now=True)),
            ],
        ),
    ]
