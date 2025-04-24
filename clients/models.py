from django.db import models

# Create your models here.

class HealthProgram(models.Model):
    """
    Model representing a health program.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Client(models.Model):
    """
    Model representing a client.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=10)  # Format: YYYY-MM-DD
    Gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F','Female')])
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    health_program = models.ForeignKey(HealthProgram, on_delete=models.CASCADE, related_name='clients', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

