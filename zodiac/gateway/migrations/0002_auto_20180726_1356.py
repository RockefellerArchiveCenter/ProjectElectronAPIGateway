# Generated by Django 2.0 on 2018-07-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceregistry',
            name='service_route_port',
        ),
        migrations.AddField(
            model_name='application',
            name='service_port',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]