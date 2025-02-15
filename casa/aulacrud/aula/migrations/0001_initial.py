# Generated by Django 5.0 on 2024-10-07 12:00

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(max_length=100)),
                ('numero_quartos', models.IntegerField(default=1)),
                ('area', models.FloatField()),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.pessoa')),
            ],
        ),
    ]
