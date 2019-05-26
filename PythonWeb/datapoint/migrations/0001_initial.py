# Generated by Django 2.2 on 2019-04-14 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
            ],
        ),
    ]