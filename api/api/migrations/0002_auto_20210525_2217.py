# Generated by Django 3.2.3 on 2021-05-25 13:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comparison',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]