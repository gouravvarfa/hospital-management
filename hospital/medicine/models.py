from django.db import models

# Model for Medicine Request (Doctor to Medical Store)
class MedicalRequest(models.Model):
    doctor_name = models.CharField(max_length=200)
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied'), ('Forwarded to Supplier', 'Forwarded to Supplier')],
        default='Pending'
    )

    def __str__(self):
        return f"Request from Dr. {self.doctor_name} for {self.quantity} {self.medicine_name}"


# Model for External Supplier Request (Medical Store to Supplier)
class ExternalRequest(models.Model):
    medicine_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date_requested = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')],
        default='Pending'
    )

    def __str__(self):
        return f"External Request for {self.quantity} {self.medicine_name}"
