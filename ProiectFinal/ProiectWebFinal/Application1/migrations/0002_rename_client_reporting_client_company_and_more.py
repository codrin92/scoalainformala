# Generated by Django 4.0.4 on 2022-06-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporting',
            name='assigned_engineer',
            field=models.CharField(choices=[('Codrin Florescu', 'Codrin Florescu'), ('Dragos Popescu', 'Dragos Popescu')], default='NA', max_length=45),
        ),
        migrations.AddField(
            model_name='reporting',
            name='building_height',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='client_representative',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reporting',
            name='number_of_stairs',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='project_fee',
            field=models.CharField(default='NA', max_length=10),
        ),
        migrations.AddField(
            model_name='reporting',
            name='project_value',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='quote_accepted',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='quote_issued',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='quote_produced',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='report_generated',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='reporting',
            name='request_date',
            field=models.CharField(default='2022-06-05', max_length=100),
        ),
    ]
