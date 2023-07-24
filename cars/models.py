from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='car_brand'
    )
    factory_year = models.CharField(blank=True, null=True)
    model_year = models.CharField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=2)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model

    """ def save(self, *args, **kwargs):
        self.value = round(self.value, 2) # type: ignore
        super(Car, self).save(*args, **kwargs)
     """


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.DecimalField(null=True, max_digits=30, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Car Inventory"


    def __str__(self):
        return (f'{self.cars_count} --> {self.cars_value}')
