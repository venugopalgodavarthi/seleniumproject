from django.db import models

class universitymodel(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class collegemodel(models.Model):
    cname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()
    noofstudents = models.IntegerField()
    website = models.URLField()
    email = models.EmailField()
    noofstaff = models.IntegerField()
    university = models.ForeignKey(
        universitymodel, on_delete=models.CASCADE)

    def __str__(self):
        return self.cname
