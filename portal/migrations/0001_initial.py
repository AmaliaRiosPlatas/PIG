# Generated by Django 3.2 on 2023-06-15 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=80, verbose_name='Apellido')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('domicilio', models.CharField(max_length=80, verbose_name='Domicilio')),
                ('email', models.CharField(max_length=30, verbose_name='Email de contacto')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('usuario', models.CharField(max_length=30, verbose_name='Usuario')),
                ('contrasenia', models.CharField(max_length=30, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Vacunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacunas', models.CharField(max_length=30, verbose_name='Vacunas')),
            ],
        ),
        migrations.CreateModel(
            name='Veterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Veterinaria')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=30, verbose_name='Nombre del servicio')),
                ('veterinaria', models.ManyToManyField(to='portal.Veterinaria', verbose_name='Veterinaria')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('raza', models.CharField(max_length=50, verbose_name='Raza')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('tamanio', models.CharField(max_length=50, verbose_name='Tamanio')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.cliente', verbose_name='Cliente')),
                ('vacunas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.vacunas', verbose_name='Vacunas')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='veterinaria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.veterinaria'),
        ),
    ]
