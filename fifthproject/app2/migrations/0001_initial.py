# Generated by Django 4.2.6 on 2023-11-07 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=30)),
            ],
        ),
    ]
