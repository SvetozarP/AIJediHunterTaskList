from django.db import models

# Create your models here.

class Task(models.Model):
    planet_name = models.CharField(max_length=255)
    character_name = models.CharField(max_length=255)
    ship_name = models.CharField(max_length=255)
    verb = models.CharField(max_length=20, default="hunt")  # add this
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.verb} {self.character_name} on {self.planet_name} using {self.ship_name}"