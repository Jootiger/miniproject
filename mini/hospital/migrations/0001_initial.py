# Generated by Django 2.1.3 on 2018-11-05 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='NAME')),
                ('pid', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Patient ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('createDate', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('modifyDate', models.DateTimeField(auto_now=True, verbose_name='Modify Date')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'info',
                'ordering': ('-modifyDate',),
                'db_table': 'hospital_patients',
            },
        ),
    ]
