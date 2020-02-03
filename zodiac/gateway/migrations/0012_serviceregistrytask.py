# Generated by Django 2.0 on 2018-10-22 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0011_auto_20181018_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRegistryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('async_result_id', models.CharField(max_length=40)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateway.ServiceRegistry')),
            ],
        ),
    ]