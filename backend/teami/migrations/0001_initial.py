# Generated by Django 3.2.15 on 2022-08-05 06:09

from django.db import migrations, models
import django.db.models.deletion
import django_prometheus.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('toxicity', models.CharField(max_length=20)),
                ('prohibit_period', models.CharField(max_length=50)),
                ('prohibit_area', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'fish',
            },
            bases=(django_prometheus.models.ExportModelOperationsMixin('fish'), models.Model),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('fish', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fish_id', to='teami.fish')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='teami.user')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
