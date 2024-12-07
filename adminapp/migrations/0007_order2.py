# Generated by Django 5.1.1 on 2024-12-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('total_cost', models.IntegerField()),
            ],
        ),
    ]
