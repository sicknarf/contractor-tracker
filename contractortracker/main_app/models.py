from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.



class Client(models.Model):
    name = models.CharField(
        "Client Name",
        max_length=30)
    address1 = models.CharField(
        "Address line 1",
        max_length=100,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=100,
        blank=True
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=100,
    )
    state = models.CharField(
        "State",
        max_length=2,
    )

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    new_line = '\n'
    def __str__(self):
        return f"{self.name}{self.address1}{self.new_line}{self.address2}{self.city}, {self.state} {self.zip_code}"
    created_time = models.DateTimeField('date created', default=timezone.now)

class Task(models.Model):
    description = models.TextField(max_length=2048)
    complete = models.BooleanField(default=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        if len(self.description) > 15:
            return f"{self.description[:15]}..."
        else:
            return f"{self.description}"