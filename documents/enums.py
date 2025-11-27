from django.db.models import TextChoices

class DocumentType(TextChoices):
    CERTIFICATE = "certificate", "Certificate"
    INSURANCE = "insurance", "Insurance"
    MAINTENANCE = "maintenance", "Maintenance"
    INSPECTION = "inspection", "Inspection"
