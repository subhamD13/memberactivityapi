# Generated by Django 3.0.5 on 2020-07-30 16:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tz', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=60)),
                ('activity_periods', models.ManyToManyField(to='activityapi.Activity')),
                ('tz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='activityapi.Timezone')),
            ],
        ),
    ]
