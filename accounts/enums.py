from django.db.models import TextChoices

class PropertyTypeChoices(TextChoices):
    HOUSE = 'house', 'House'
    BUNGALOW = 'bungalow', 'Bungalow'
    FLAT = 'flat', 'Flat'
    OTHER = 'other', 'Other'
    ADMIN = 'admin', 'Admin'    

