from django.db import models

# Create your models here.

# Business model 
class Business(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name

class Appointment(models.Model):
    business = models.ForeignKey(Business, related_name = "appointments",  on_delete = models.CASCADE)
    customer_name = models.CharField(max_length = 200)
    service = models.CharField(max_length = 100)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled')


    def __str__(self):
        return f'{self.customer_name} - {self.service} at {self.date_time}'
