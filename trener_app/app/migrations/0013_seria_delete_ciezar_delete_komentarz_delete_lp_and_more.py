# Generated by Django 4.2.9 on 2024-01-16 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_ciezar_powtorzenia_delete_ciężar_delete_powtórzenia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ilosc_powtorzen', models.IntegerField(default=0)),
                ('ilosc_serii', models.IntegerField(default=0)),
                ('obciazenie', models.DecimalField(decimal_places=1, default=0, max_digits=500)),
                ('uwagi', models.TextField()),
                ('tempo', models.CharField(max_length=10)),
                ('nagraj', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ciezar',
        ),
        migrations.DeleteModel(
            name='Komentarz',
        ),
        migrations.DeleteModel(
            name='LP',
        ),
        migrations.DeleteModel(
            name='Nagranie',
        ),
        migrations.DeleteModel(
            name='powtorzenia',
        ),
        migrations.DeleteModel(
            name='Serie',
        ),
        migrations.DeleteModel(
            name='Tempo',
        ),
        migrations.RemoveField(
            model_name='cwiczenie',
            name='link',
        ),
        migrations.AddField(
            model_name='cwiczenie',
            name='opis',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cwiczenie',
            name='video_url',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seria',
            name='cwiczenie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cwiczenie'),
        ),
    ]
