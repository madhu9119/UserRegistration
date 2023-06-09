# Generated by Django 3.2.16 on 2023-03-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('loginid', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
    ]
