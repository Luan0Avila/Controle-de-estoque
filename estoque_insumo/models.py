from django.db import models

class Material(models.Model):
    code = models.IntegerField(primary_key=True, max_length=7, unique=True)
    description = models.TextField(max_length=65)

    def __str__(self):
        return self.code

class Position(models.Model):
    ...
    
