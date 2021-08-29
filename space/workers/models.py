import uuid

from django.db import models
from django.urls import reverse

# Create your models here.

class FieldWorker(models.Model):
    FUNCTION_CHOICES = [
        ('Harvest', 'Harvest'),
        ('Pruning', 'Pruning'),
        ('Scouting', 'Scouting'),
        ('Other', 'Other')
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    function = models.CharField(
        max_length=50,
        default='Other',
        choices=FUNCTION_CHOICES
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "fieldworker"
        verbose_name_plural = "fieldworkers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
