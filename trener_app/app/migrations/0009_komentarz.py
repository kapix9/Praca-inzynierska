# Generated by Django 4.2.9 on 2024-01-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_lp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentarz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Kom', models.CharField(max_length=255)),
            ],
        ),
    ]