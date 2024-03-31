from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.contrib.auth.hashers import make_password





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
    body_part = models.CharField(max_length=20,
                                 choices=BODY_PART_CHOICES)

    def __str__(self):
        return self.movement_name
    

class move(models.Model):
    exercise = models.ForeignKey(ExersiseAdd, on_delete=models.CASCADE)
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    rest_duration = models.DurationField()


# Signal handler function to create exercises for the authenticated user

