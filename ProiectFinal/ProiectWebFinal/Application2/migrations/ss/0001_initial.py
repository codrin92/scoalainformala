# Generated by Django 4.0.4 on 2022-06-04 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Application1', '0011_reporting_project_fee_alter_reporting_request_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenues',
            fields=[
                ('project_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Application1.reporting')),
            ],
        ),
    ]
