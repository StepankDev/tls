from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name

class ContactRent(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name

class ContactPartner(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
