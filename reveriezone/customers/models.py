from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))

    STATE_CHOICES = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CG', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TS', 'Telangana'),
    ('TR', 'Tripura'),
    ('UK', 'Uttarakhand'),
    ('UP', 'Uttar Pradesh'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DH', 'Dadra and Nagar Haveli'),
    ('DD', 'Daman and Diu'),
    ('DL', 'Delhi'),
    ('LD', 'Lakshadweep'),
    ('PY', 'Puducherry'),
    ]


    location_choices = [
        ('Home (All day delivery)', 'Home'),
        ('Workplace (delivery between 10AM-6PM)', 'Workplace'),
    ]

    name=models.CharField(max_length=200)
    address=models.TextField()
    pincode=models.CharField(max_length=6)
    city=models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default='AL')
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='customer_profile')
    phone=models.CharField(max_length=10)
    location = models.CharField(max_length=40, choices=location_choices)
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title