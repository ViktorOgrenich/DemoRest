from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Car(models.Model):
    make = models.CharField(verbose_name='Make', db_index=True, max_length=80)
    model = models.CharField(verbose_name='Model', max_length=80)
    color = models.CharField(verbose_name='Color', max_length=80)
    CAR_BODY = (
        (1, 'Coupe'),
        (2, 'Sedan'),
        (3, 'Hatchback'),
        (4, 'Wagon'),
    )
    car_body = models.IntegerField(verbose_name='CAR_BODY', choices=CAR_BODY)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)