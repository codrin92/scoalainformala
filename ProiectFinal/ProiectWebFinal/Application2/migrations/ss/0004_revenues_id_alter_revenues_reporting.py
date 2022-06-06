# Generated by Django 4.0.4 on 2022-06-05 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application1', '0012_alter_reporting_request_date'),
        ('Application2', '0003_alter_revenues_reporting'),
    ]

    operations = [
        migrations.AddField(
            model_name='revenues',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='revenues',
            name='reporting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Application1.reporting'),
        ),
    ]