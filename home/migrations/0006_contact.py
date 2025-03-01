# Generated by Django 3.2.11 on 2022-02-07 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge_0001_devise_unit_0004_agences'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='User Name')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='User Phone')),
                ('subject', models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject')),
                ('message', models.CharField(blank=True, max_length=255, null=True, verbose_name='Message')),
                ('is_read', models.BooleanField(default=False, verbose_name='Is Read')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
