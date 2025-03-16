from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Construction(models.Model):
    ConstructionType = models.CharField(max_length=200)
    ConstructionName = models.CharField(max_length=200)
    CementQuality = models.CharField(max_length=200)
    CementPrice = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(200)],default=0)
    BrickQuality = models.CharField(max_length=200)
    BrickPrice = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(20)],default=0)
    SandQuality = models.CharField(max_length=200)
    SandPrice = models.IntegerField(validators=[MaxValueValidator(500), MinValueValidator(200)],default=0)
    IronQuality = models.CharField(max_length=200)
    IronPrice = models.IntegerField(validators=[MaxValueValidator(50000), MinValueValidator(20000)], default=0)
    EnvironmentalCondition = models.CharField(max_length=100)
    Seller = models.CharField(max_length=500)
    Price = models.BigIntegerField(validators=[MaxValueValidator(5000000), MinValueValidator(2000000)],default=0)

    def __str__(self):
        return f"{self.ConstructionType} {self.ConstructionName}"


