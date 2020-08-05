# Generated by Django 2.2.3 on 2020-08-05 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_categoria_jogos_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogos',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='system.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='ganhador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_ganhador', to='system.Usuario', verbose_name='Ganhador'),
        ),
        migrations.AlterField(
            model_name='jogos',
            name='pontos',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Pontos Recebidos'),
        ),
    ]
