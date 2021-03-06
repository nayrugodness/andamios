# Generated by Django 3.1.2 on 2021-11-05 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('vertical', models.IntegerField(choices=[[0, 'Design'], [1, 'Data'], [2, 'Software'], [3, 'Marketing'], [4, 'Blockchain']])),
                ('states', models.IntegerField(choices=[[0, 'Studying'], [1, 'Applying'], [2, 'Working'], [3, 'Stopped']])),
                ('talentSize', models.CharField(max_length=100)),
                ('country', models.TextField(max_length=30)),
                ('photo', models.ImageField(null=True, upload_to='media')),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='moduloprincipal.token')),
            ],
        ),
    ]
