# Generated by Django 2.0 on 2018-10-05 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gateway', '0008_serviceregistry_callback_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.CharField(max_length=4)),
                ('request_url', models.URLField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='serviceregistry',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='requestlog',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateway.ServiceRegistry'),
        ),
    ]