from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.core.validators import MinValueValidator




# 

Gender = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Not specified'),
)


WeightUnits = (
    (0, 'KG'),
    (1, 'Pound')
)


# Create your models here.


class MainUser(AbstractUser):
    
    #username: نام کاربری کاربر.
    #first_name: نام کاربر.
    #last_name: نام خانوادگی کاربر.
    #email: ایمیل کاربر.
    #password: رمز عبور کاربر.
    #is_active: مشخص کننده فعال بودن حساب کاربری.
    #is_staff: مشخص کننده اینکه آیا کاربر به عنوان کارمند (staff) در نظام مدیریت سایت است یا خیر.
    #is_superuser: مشخص کننده اینکه آیا کاربر دسترسی مدیریتی فوق العاده (superuser) دارد یا خیر.
    #date_joined: تاریخ عضویت کاربر در سیستم.
    #last_login: تاریخ آخرین ورود کاربر به سیستم.

    PhoneNumber = models.CharField(max_length=15, null=True, blank=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('not_specific', 'Not Specific'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='not_specific')
    UserHeight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    height_unit = models.CharField(max_length=2, choices=[('cm', 'cm'), ('in', 'in')], default='cm')
    UserWeight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)])
    WEIGHT_UNIT_CHOICES = [
        ('kg', 'kg'),
        ('lb', 'lb'),
    ]
    weight_unit = models.CharField(max_length=2, choices=WEIGHT_UNIT_CHOICES, default='kg')
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

