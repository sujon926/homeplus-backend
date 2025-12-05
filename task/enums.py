from django.db.models import TextChoices

class EventType(TextChoices):
    MAINTENANCE = "maintenance", "Maintenance"
    INSPECTION = "inspection", "Inspection"
    ADMIN = "admin", "Admin"
    SAFETY = "safety", "Safety"

class Priority(TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"

class ComplianceType(TextChoices):
    NONE = "none", "None"
    GAS_SAFETY = "gas_safety", "Gas Safety"
    EICR = "eicr", "EICR"
    EPC = "epc", "EPC"
