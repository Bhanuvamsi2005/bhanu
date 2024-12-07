# Generated by Django 5.1.1 on 2024-10-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_studentlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('quality_of_service', models.IntegerField()),
                ('website_interface', models.IntegerField()),
                ('overall_experience', models.IntegerField()),
            ],
        ),
    ]
