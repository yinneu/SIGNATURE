# Generated by Django 2.2.4 on 2023-08-23 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_auto_20230822_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='hdd',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='vos',
        ),
        migrations.RemoveField(
            model_name='vos',
            name='name',
        ),
        migrations.AddField(
            model_name='vos',
            name='hdd',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='vos',
            name='os_type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vos',
            name='ram',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='vos',
            name='vc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.Vaccine'),
        ),
    ]