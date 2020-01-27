# Generated by Django 2.0 on 2018-10-04 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0002_auto_20180726_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='application',
            name='modified_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='service_port',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]