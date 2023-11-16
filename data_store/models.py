from django.db import models


# Create your models here.

class nameChoices(models.IntegerChoices):
    temperature = 1, 'Temperature'
    ph = 2, 'PH Value'
    stirring_speed = 3, 'Stirring Speed'


class Record(models.Model):
    value = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Record Value")
    time = models.DateTimeField(auto_now=True, verbose_name="Record Time")
    name = models.SmallIntegerField(choices=nameChoices.choices, verbose_name="Sub System")

    class Meta:
        verbose_name = verbose_name_plural = 'Record for Bioreactor'

    def __str__(self):
        return f'{self.id}'


class DesiredValues(models.Model):
    desired_value = models.DecimalField(max_digits=6, decimal_places=1, verbose_name="Desired Value")
    name = models.SmallIntegerField(choices=nameChoices.choices, verbose_name="Sub System", unique=True,
                                    primary_key=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Desired Values for Bioreactor'

    def __str__(self):
        return f'{self.name}'
