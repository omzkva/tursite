# Generated by Django 4.1.1 on 2022-09-06 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kind_transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity_place', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('distance_air', models.IntegerField()),
                ('picture', models.ImageField(upload_to=None)),
                ('check_tur', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('num_tran', models.IntegerField()),
                ('description', models.TextField()),
                ('check_tur', models.BooleanField(default=False)),
                ('kind_tran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.kind_transport')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.region'),
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('pic_cart', models.ImageField(upload_to=None)),
                ('url', models.URLField(max_length=500)),
                ('price', models.IntegerField()),
                ('check_tur', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.location')),
            ],
        ),
        migrations.CreateModel(
            name='Foot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitchen', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price_day', models.IntegerField()),
                ('check_tur', models.BooleanField(default=False)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turist.location')),
            ],
        ),
    ]