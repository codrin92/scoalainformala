# Generated by Django 4.0.4 on 2022-06-05 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application1', '0012_alter_reporting_request_date'),
        ('Application2', '0002_remove_revenues_project_name_revenues_reporting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revenues',
            name='reporting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Application1.reporting'),
        ),
    ]
