# Generated by Django 5.1.1 on 2024-09-13 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_alter_historicalproduto__change_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduto',
            name='_change_reason',
            field=models.CharField(blank=True, default='Criar', max_length=255, verbose_name='Razão da alteração'),
        ),
        migrations.AlterField(
            model_name='historicalproduto',
            name='categoria',
            field=models.CharField(choices=[('E', 'Eletronicos'), ('D', 'Domésticos'), ('CMB', 'Cama, Mesa e Banho')], max_length=5),
        ),
        migrations.AlterField(
            model_name='produto',
            name='_change_reason',
            field=models.CharField(blank=True, default='Criar', max_length=255, verbose_name='Razão da alteração'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('E', 'Eletronicos'), ('D', 'Domésticos'), ('CMB', 'Cama, Mesa e Banho')], max_length=5),
        ),
    ]