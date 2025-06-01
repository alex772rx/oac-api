from django.db import models

class Sales(models.Model):
    ASSIGNED_CHOICES = [
        ('Santosh', 'Santosh'),
        ('Shiva', 'Shiva'),
        ('Neither', 'Neither'),
    ]

    IMPLANTS_TYPES = [
        ('SS', 'SS'),
        ('TITANIUM', 'TITANIUM'),
        ('Neither', 'Neither'),
    ]

    date = models.DateField()
    bill_no = models.CharField(max_length=50)
    implants_name = models.TextField()
    implants_type = models.CharField(choices=IMPLANTS_TYPES)
    size = models.IntegerField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    assigned = models.CharField(max_length=10, choices=ASSIGNED_CHOICES)
    institute = models.CharField(max_length=100)
    surgeon = models.CharField(max_length=100)
    remarks = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.rate
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.bill_no} - {self.date}"
