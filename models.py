from django.db import models
from django.utils import timezone

# Model is a blueprint of a table (db representation)
# models is classes/methods that you use to work with that table. 

class EmergencyLight(models.Model):
    # class EmergencyLight(models.Model): defines a new model called EmergencyLight that inherits from Django's Model class.

    # name = models.CharField(max_length=50) defines a new field called name that is a CharField with a maximum length of 50 characters.
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    battery_level = models.IntegerField(default=100)
    last_reported = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name