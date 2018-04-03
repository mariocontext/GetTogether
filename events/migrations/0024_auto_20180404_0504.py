# Generated by Django 2.0 on 2018-04-04 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0023_add_searchable_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='last_reminded',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date Created'),
        ),
    ]
