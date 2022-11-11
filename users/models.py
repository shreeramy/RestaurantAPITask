from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserAccountManager

class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_restraunt = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to="profile_pic/", 
                                    blank=True, 
                                    null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserAccountManager()

    def __str__(self):
        return self.email


from restrant.models import Restraunt
class Employee(BaseModel):
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                blank=True, null=True)
    salary = models.PositiveBigIntegerField(blank=True, null=True)