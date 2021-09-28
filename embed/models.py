from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    
    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
        
    def __str__(self):
        return self.title


class PharmaDetails(models.Model):
    AWBnumber = models.CharField(max_length=100)
    beaconId = models.IntegerField()
    description = models.CharField(max_length=100)
    temperature = models.CharField(max_length=20)
    
    def __str__(self):
        return self.AWBnumber


class PharmaComponents(models.Model):
    AWBnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
