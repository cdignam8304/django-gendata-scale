from django.db import models
# from django.utils import timezone
import os
from django.conf import settings

# Useful tutorial for database indexing and other db commands
# https://www.sqlitetutorial.net/sqlite-index/


# Create your models here.
    
    
class Schema(models.Model):
    schema_name = models.CharField("schema name", max_length=200, blank=False)
    schema_description = models.CharField("schema_description", max_length=200, blank=True)
    string1 = models.CharField("string1", max_length=200, blank=False)
    string2 = models.CharField("string2", max_length=200, blank=True)
    string3 = models.CharField("string3", max_length=200, blank=True)
    string4 = models.CharField("string4", max_length=200, blank=True)
    string5 = models.CharField("string5", max_length=200, blank=True)
    string6 = models.CharField("string6", max_length=200, blank=True)
    string7 = models.CharField("string7", max_length=200, blank=True)
    string8 = models.CharField("string8", max_length=200, blank=True)
    string9 = models.CharField("string9", max_length=200, blank=True)
    string10 = models.CharField("string10", max_length=200, blank=True)
    date1 = models.CharField("date1", max_length=200, blank=True)
    date2 = models.CharField("date2", max_length=200, blank=True)
    date3 = models.CharField("date3", max_length=200, blank=True)
    date4 = models.CharField("date4", max_length=200, blank=True)
    date5 = models.CharField("date5", max_length=200, blank=True)
    float1 = models.CharField("float1", max_length=200, blank=True)
    float2 = models.CharField("float2", max_length=200, blank=True)
    float3 = models.CharField("float3", max_length=200, blank=True)
    float4 = models.CharField("float4", max_length=200, blank=True)
    float5 = models.CharField("float5", max_length=200, blank=True)
    int1 = models.CharField("int1", max_length=200, blank=True)
    int2 = models.CharField("int2", max_length=200, blank=True)
    int3 = models.CharField("int3", max_length=200, blank=True)
    int4 = models.CharField("int4", max_length=200, blank=True)
    int5 = models.CharField("int5", max_length=200, blank=True)
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
    string6 = models.CharField("string6", max_length=200, blank=True)
    string7 = models.CharField("string7", max_length=200, blank=True)
    string8 = models.CharField("string8", max_length=200, blank=True)
    string9 = models.CharField("string9", max_length=200, blank=True)
    string10 = models.CharField("string10", max_length=200, blank=True)
    date1 = models.DateField("date1", default=None, blank=True, null=True)
    date2 = models.DateField("date2", default=None, blank=True, null=True)
    date3 = models.DateField("date3", default=None, blank=True, null=True)
    date4 = models.DateField("date4", default=None, blank=True, null=True)
    date5 = models.DateField("date5", default=None, blank=True, null=True)
    float1 = models.DecimalField("float1", decimal_places=2, max_digits=10, blank=True, null=True)
    float2 = models.DecimalField("float2", decimal_places=2, max_digits=10, blank=True, null=True)
    float3 = models.DecimalField("float3", decimal_places=2, max_digits=10, blank=True, null=True)
    float4 = models.DecimalField("float4", decimal_places=2, max_digits=10, blank=True, null=True)
    float5 = models.DecimalField("float5", decimal_places=2, max_digits=10, blank=True, null=True)
    int1 = models.IntegerField("int1", blank=True, null=True)
    int2 = models.IntegerField("int2", blank=True, null=True)
    int3 = models.IntegerField("int3", blank=True, null=True)
    int4 = models.IntegerField("int4", blank=True, null=True)
    int5 = models.IntegerField("int5", blank=True, null=True)
    status = models.CharField("status", max_length=10, choices=STATUS, default=OPEN)
    created_at = models.DateTimeField("created", auto_now_add=True)
    last_updated = models.DateTimeField("updated", auto_now=True)
    
    
    class Meta():
        verbose_name_plural = "Generic Datasets"
    
    def __str__(self):
        return f"{self.schema_name}: {self.string1}"
    
    

class Report(models.Model):
    name = models.CharField("name", max_length=200, blank=False)
    description = models.CharField("description", max_length=200, blank=False)
    
    class Meta():
        verbose_name_plural = "Reports"
        
    def __str__(self):
        return f"{self.name}: {self.description}"
    


