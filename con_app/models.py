from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import TextField


class EnvironmentalCondition(models.Model):
    condition = models.CharField(max_length=100, unique=True)
    precations=models.TextField(max_length=10000,default=None)

    def __str__(self):
        return self.condition


class Seller(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=300, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    details= models.TextField(blank=True,null=True,default="No details Provided")

    def __str__(self):
        return self.name


class Construction(models.Model):
    ConstructionType = models.CharField(max_length=200)
    ConstructionName = models.CharField(max_length=200)
    CementQuality = models.CharField(max_length=200)
    CementPrice = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(200)], default=200)
    BrickQuality = models.CharField(max_length=200)
    BrickPrice = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(20)], default=20)
    SandQuality = models.CharField(max_length=200)
    SandPrice = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(200)], default=200)
    IronQuality = models.CharField(max_length=200)
    IronPrice = models.IntegerField(validators=[MaxValueValidator(50000), MinValueValidator(20000)], default=20000)

    # ForeignKey relations
    EnvironmentalCondition = models.ForeignKey(EnvironmentalCondition, on_delete=models.SET_NULL, null=True)
    Seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)

    Price = models.BigIntegerField(validators=[MaxValueValidator(5000000), MinValueValidator(2000000)], default=2000000)

    def __str__(self):
        return f"{self.ConstructionType} {self.ConstructionName}"
