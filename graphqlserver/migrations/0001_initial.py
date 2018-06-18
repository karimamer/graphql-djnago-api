# Generated by Django 2.0.6 on 2018-06-18 04:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mac_address', models.CharField(max_length=48)),
                ('os', models.CharField(max_length=100)),
                ('os_version', models.FloatField()),
                ('device_type', models.CharField(choices=[(1, 'phone'), (2, 'laptop'), (3, 'tablet')], max_length=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='graphqlserver.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('plan_type', models.CharField(choices=[(1, 'Monthly'), (2, 'Traveler'), (3, 'Weekly')], default='MONTHLY', max_length=9)),
                ('start_date', models.DateTimeField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_owner', to='graphqlserver.Customer')),
            ],
        ),
    ]