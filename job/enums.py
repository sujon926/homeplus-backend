from django.db import models

class ServiceTypeChoices(models.TextChoices):
    PLUMBING = 'Plumbing', 'Plumbing'
    HEATING = 'Heating', 'Heating'
    ELECTRICAL = 'Electrical', 'Electrical'
    GARDENING = 'Gardening', 'gardening'
    CLEANING = 'Cleaning', 'cleaning'
    OTHERS = 'Others', 'Others'

class PriorityChoices(models.TextChoices):
    LOW = 'Low', 'Low'
    MEDIUM = 'Medium', 'Medium'
    HIGH = 'High', 'High'
