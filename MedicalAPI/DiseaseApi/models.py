from django.db import models

# Create your models here.
class PatientDetails(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=70, null=True, blank=True)
    symptoms = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{},{},{},{}'.format(self.name, self.phone, self.email, self.symptoms, self.created)

