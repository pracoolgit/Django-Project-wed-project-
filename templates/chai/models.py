from django.db import models
from django.utils import timezone

# Create your models here.
class chaivarity(models.Model):
    CHAI_TYPE_CHOICE=[
        ('BL','BLACK'),
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
        

    ]
    name=models.charFeild(max_length=100)
    image=models.ImageField(upload_to='cgais/')
    date_added=models.datetimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
