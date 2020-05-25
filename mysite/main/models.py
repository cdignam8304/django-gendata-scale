from django.db import models
from django.utils import timezone
import os
from django.conf import settings

# Useful tutorial for database indexing and other db commands
# https://www.sqlitetutorial.net/sqlite-index/


# Create your models here.
    
    
class Schema(models.Model):
    schema_name = models.CharField("schema name", max_length=200, blank=False)
    string1 = models.CharField("string1", max_length=200, blank=False)
    string2 = models.CharField("string2", max_length=200, blank=True)
    string3 = models.CharField("string3", max_length=200, blank=True)
    string4 = models.CharField("string4", max_length=200, blank=True)
    string5 = models.CharField("string5", max_length=200, blank=True)
    date1 = models.CharField("date1", max_length=200, blank=True)
    date2 = models.CharField("date2", max_length=200, blank=True)
    date3 = models.CharField("date3", max_length=200, blank=True)
    amount1 = models.CharField("amount1", max_length=200, blank=True)
    amount2 = models.CharField("amount2", max_length=200, blank=True)
    status = models.CharField("status", max_length=200, blank=True)
    photo = models.ImageField(upload_to="media",
                                     default = os.path.join(settings.MEDIA_URL,"placeholder.jpeg"))
    
    class Meta():
        verbose_name_plural = "Schemas"
        
    def __str__(self):
        return self.schema_name
    
    

class Generic(models.Model):
    
    OPEN = 'OPEN'
    ACCEPTED = 'ACCEPTED'
    REJECTED = "REJECTED"
    DEFERRED = "DEFERRED"
    ESCALATED = "ESCALATED"
    
    STATUS = [
        (OPEN, 'Open'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (DEFERRED, 'Deferred'),
        (ESCALATED, 'Escalated')
    ]
    
    schema_name = models.ForeignKey(Schema,
                                    default=None,
                                    verbose_name="schema name",
                                    on_delete=models.SET_DEFAULT)
    string1 = models.CharField("string1", max_length=200, blank=False)
    string2 = models.CharField("string2", max_length=200, blank=True)
    string3 = models.CharField("string3", max_length=200, blank=True)
    string4 = models.CharField("string4", max_length=200, blank=True)
    string5 = models.CharField("string5", max_length=200, blank=True)
    date1 = models.DateField("date1", default=None, blank=True, null=True)
    date2 = models.DateField("date2", default=None, blank=True, null=True)
    date3 = models.DateField("date3", default=None, blank=True, null=True)
    amount1 = models.DecimalField("amount1", decimal_places=2, max_digits=10, blank=True, null=True)
    amount2 = models.DecimalField("amount2", decimal_places=2, max_digits=10, blank=True, null=True)
    status = models.CharField("status", max_length=10, choices=STATUS, default=OPEN)
    created_at = models.DateTimeField("created", auto_now_add=True)
    last_updated = models.DateTimeField("updated", auto_now=True)
    
    
    class Meta():
        verbose_name_plural = "Generic Datasets"
    
    def __str__(self):
        return f"{self.schema_name}: {self.string1}"
    
    
    # This isn't being applied in the form
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return [
                "schema_name",
                ]
        else:
            return []