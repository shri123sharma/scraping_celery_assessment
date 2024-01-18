from django.db import models

class JobData(models.Model):
    ip_address = models.CharField(max_length=100,null=True,blank=True)
    port = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    protocols = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.country