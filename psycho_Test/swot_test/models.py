from django.db import models
import uuid

class StudentDetail(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone =models.IntegerField(null=True )
    alt_phone = models.IntegerField(null=True)
    pdf_link = models.URLField(null=True, blank=True) 
    
    def __str__(self):
        return self.email

    
# Create your models here.
class Question(models.Model):
    # question_id = models.IntegerField(null=True)
    question_text = models.TextField()  # The actual question
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    attribute = models.CharField(max_length=50)  # e.g., 
    
    def __str__(self):
        return self.attribute
    
    
class CareerFields(models.Model):
    field_name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True,default="NULL")
    opportunity = models.TextField(blank=True,default="NULL")
    threat = models.TextField(blank=True,default="NULL")
    strength_weakness = models.TextField(null=True,blank=True,default="NULL")
    example1 = models.TextField(blank=True,null=True,default="NULL")
    example2 = models.TextField(blank=True,null=True,default="NULL")
    
    def __str__(self):
        return self.field_name
    
    
class StrengthWeakness(models.Model):
    attribute= models.CharField(max_length=225)
    at_strength = models.TextField(blank=True)
    at_weakness = models.TextField(blank=True)
    profile = models.TextField(blank=True)
    
    def __str__(self):
        # Return a meaningful string, for example, the attribute or combination of fields
        return f"Strength/Weakness: {self.attribute} - Strength: {self.at_strength[:30]}... - Weakness: {self.at_weakness[:30]}..."






