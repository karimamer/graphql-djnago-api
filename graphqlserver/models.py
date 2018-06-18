from django.db import models
import uuid

DEVICE_TYPE = (
    ('phone','phone' ),
    ('laptop', 'laptop'),
    ('tablet', 'tablet'),
)

PLAN = (
    ('Monthly', 'Monthly'),
    ('Travler','Travler'),
    ('Weekly', 'Weekly'),
)

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mac_address = models.CharField(max_length=48)
    os = models.CharField(max_length=100)
    os_version = models.FloatField()
    device_type = models.CharField(choices=DEVICE_TYPE, max_length=10)
    customer_id = models.ForeignKey(Customer, related_name='customers', on_delete=models.CASCADE)



class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    plan_type = models.CharField(choices=PLAN,max_length=9, default='MONTHLY')
    start_date = models.DateTimeField()
    customer_id = models.OneToOneField(Customer, related_name='plan_owner', on_delete=models.CASCADE)
