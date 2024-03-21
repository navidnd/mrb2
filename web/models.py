from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date



# 

Gender = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not specified'),
)

HeightUnits = (
    (0, 'Cm'),
    (1, 'Inch')
)

WeightUnits = (
    (0, 'KG'),
    (1, 'Pound')
)


# Create your models here.


class MainUser(AbstractUser):
    
    FirstName = models.CharField(max_length=128)
    LastName = models.CharField(max_length=128)
    PhoneNumber = models.CharField(max_length=128)
    gender = models.IntegerField(choices=Gender)
    UserHeight = models.SmallIntegerField()
    UserWeight = models.SmallIntegerField()
    BirthDate = models.DateField(null=True, blank=True)
    


    def calculate_age(self):
        today = date.today()
        if self.BirthDate:
            return today.year - self.BirthDate.year
        return None
    

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='main_users_groups'  # Custom related_name for the groups field
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='main_users_permissions'  # Custom related_name for the user_permissions field
    )

    def __str__(self):
        return self.username
    


class ExersiseName (models.Model):

    MovementName = models.CharField(max_length=225)
    MovementPic = models.URLField()
    MovementRest = models.IntegerField
    MovementReps = models.SmallIntegerField

    # SuperSet = model. IDK!
    # TripleSet = models. IDK!
   

    def __str__(self):
        return self.MovementName


# Signal handler function to create exercises for the authenticated user

