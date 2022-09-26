# Generated by Django 4.1 on 2022-08-22 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Brand', models.CharField(max_length=100)),
                ('Address_Brand', models.CharField(max_length=1000)),
                ('Date_service', models.DateField()),
                ('software_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_web.services')),
            ],
        ),
    ]
