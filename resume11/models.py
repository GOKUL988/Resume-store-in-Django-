from django.db import models
# Create your models here.
class per(models.Model):
    perid=models.CharField(max_length=100, unique=True)
    name=models.CharField(max_length=100)
    ph_no=models.IntegerField(max_length=10)
    mail=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    sx=models.CharField(max_length=100)
    ambition=models.CharField(max_length=100)
    lan=models.CharField(max_length=100)
    add=models.CharField(max_length=500)
    def __str__(self):
        return self.perid

class aca(models.Model):
    personid = models.ForeignKey(per, on_delete=models.CASCADE)
    cs=models.CharField(max_length=100)
    sch_clg=models.CharField(max_length=500)
    uni=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    per=models.CharField(max_length=100)

class cc(models.Model):
    person1id=models.ForeignKey(per,on_delete=models.CASCADE,)
    cer=models.CharField(max_length=300)

