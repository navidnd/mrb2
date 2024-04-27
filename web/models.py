from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User




Gender = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not specified'),
)

HeightUnits = (
    (0, 'Cm'),
    (1, 'Inch')
)

WEIGHT_UNIT_CHOICES = [
        (0, 'Kilogram'),
        (1, 'Pound')
    ]

# models are here.


class MainUser(models.Model):
    
    username= models.CharField(max_length=150, default='', unique = True)
    first_name= models.CharField(max_length=30, blank=True)
    last_name= models.CharField(max_length=150, blank=True)
    email= models.EmailField(blank=False, unique=True, default='')
    password= models.CharField(max_length=150, default='')
    is_active= bool = ...
    is_staff= bool = ...
    is_superuser= bool = ...
    #date_joined= models.DateTimeField(auto_now_add=True, default='')
    #last_login: تاریخ آخرین ورود کاربر به سیستم.
    PhoneNumber = models.CharField(max_length=128)
    gender = models.IntegerField(choices=Gender)
    UserHeight = models.SmallIntegerField()
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
    


class ExersiseAdd (models.Model):

    BODY_PART_CHOICES = [
        ('foot', 'Foot'),
        ('chest', 'Chest'),
        ('biceps', 'Biceps'),
        ('triceps', 'Triceps'),
        ('shoulders', 'Shoulders'),
        ('back', 'Back'),
        ('abs', 'Abs and Core'),
        ('glutes', 'Glutes'),
    ]
    
    movement_name = models.CharField(max_length=225)
    movement_pic = models.URLField()
    body_part = models.CharField(max_length=20,choices=BODY_PART_CHOICES)

    def __str__(self):
        return self.movement_name




class MovementAdd (models.Model):
    exercise = models.ForeignKey(ExersiseAdd, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    rest_time = models.PositiveIntegerField(default=0, verbose_name='Rest Time (seconds)')

    class Meta:
        verbose_name = 'Movement'

    def __str__(self):
        return f"{self.exercise} - Repetitions: {self.repetitions} - Rest Time: {self.rest_time} seconds"



class UserWeight(models.Model):
    
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    weight = models.FloatField()
    weight_date = models.DateField(auto_now_add=True)
    target_weight = models.FloatField(null=True, blank=True)
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT_CHOICES, default='kg')

    def __str__(self):
        return f"{self.user}'s weight on {self.weight_date}"
    

class Sizes(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    biceps = models.FloatField(null=True, blank=True)
    wrist = models.FloatField(null=True, blank=True)
    chest = models.FloatField(null=True, blank=True)
    hip = models.FloatField(null=True, blank=True)
    leg = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Sizes of {self.user} recorded at {self.recorded_at}"


class Fat(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    fat_percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Fat percentage of {self.user} recorded at {self.recorded_at}"
    
class Muscle(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    muscle_percentage = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Muscle percentage of {self.user} recorded at {self.recorded_at}"
    
