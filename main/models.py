from django.db import models

class Data(models.Model):
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    contact = models.TextField()
    resources = models.TextField()
