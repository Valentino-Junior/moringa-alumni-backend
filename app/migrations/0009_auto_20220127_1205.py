# Generated by Django 3.2.9 on 2022-01-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20220127_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privatecohort',
            options={},
        ),
        migrations.RemoveField(
            model_name='privatecohort',
            name='private',
        ),
        migrations.AlterField(
            model_name='privatecohort',
            name='created_by',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='privatecohort',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='privatecohort',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='privatecohort',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]