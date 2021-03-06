# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-17 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/clientes', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/portifolio', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Portifolio',
                'verbose_name_plural': 'Portifolio',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Quem_Somos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/quem_somos', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Descrição/Foto',
                'verbose_name_plural': 'Quem Somos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Data de inicio')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/servicos', verbose_name='Imagem')),
                ('brevedescri', models.CharField(max_length=200, verbose_name='Breve Descrição')),
                ('completdescri', models.TextField(blank=True, verbose_name='Descrição Completa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
                'ordering': ['title'],
            },
        ),
    ]
