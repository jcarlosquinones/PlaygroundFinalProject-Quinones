# Generated by Django 4.2.6 on 2023-11-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pista', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('vueltas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('escuderia', models.CharField(max_length=40)),
            ],
        ),
    ]
