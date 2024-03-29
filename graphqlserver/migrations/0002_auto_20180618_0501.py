# Generated by Django 2.0.6 on 2018-06-18 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphqlserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('phone', 'phone'), ('laptop', 'laptop'), ('tablet', 'tablet')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='plan_type',
            field=models.CharField(choices=[('Monthly', 'Monthly'), ('Monthly', 'Monthly'), ('Weekly', 'Weekly')], default='MONTHLY', max_length=9),
        ),
    ]
