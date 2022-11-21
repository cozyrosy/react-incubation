# Generated by Django 4.1.3 on 2022-11-21 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_application_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.IntegerField(unique=True)),
                ('is_booked', models.BooleanField(blank=True, default=False, null=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.application')),
            ],
        ),
    ]