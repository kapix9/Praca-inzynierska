# Generated by Django 4.2.9 on 2024-01-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ciężar'),
    ]

    operations = [
        migrations.CreateModel(
            name='LP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerek', models.PositiveIntegerField()),
            ],
        ),
    ]
