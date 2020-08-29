# Generated by Django 3.0.8 on 2020-08-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('addr', models.TextField(blank=True)),
                ('schedule', models.CharField(max_length=100)),
                ('book_date', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
