# Generated by Django 2.1.3 on 2018-11-26 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('temp_today', models.FloatField(default=10)),
                ('temp_tomorrow', models.FloatField(default=10)),
                ('population', models.PositiveIntegerField()),
            ],
        ),
    ]
