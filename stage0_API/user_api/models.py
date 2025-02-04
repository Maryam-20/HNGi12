from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
import uuid


# Create your models here.

class User_details(models.Model):
    id = models.UUIDField(default= uuid.uuid1, primary_key=True, editable=False)
    email_address = models.EmailField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    github_url = models.URLField()
    
    content_type = models.ForeignKey(ContentType,  verbose_name=("content_type"), on_delete=models.CASCADE, null=True, blank=True)
    objects_id = models.PositiveIntegerField( null= True, blank=True)
    content_object = GenericForeignKey("content_type", "objects_id")
    
    def __str__(self):
        return f"{super().__str__()-{self.email_address}}"
