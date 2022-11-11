from django.db import models
from base.models import BaseModel
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Restraunt(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                              blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    logo = models.ImageField(upload_to="restraunt", blank=True, null=True)
    is_verify = models.BooleanField(default=False)

class MainMenu(BaseModel):
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)


class DailyMenu(BaseModel):
    restraunt = models.ForeignKey(Restraunt, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.PositiveBigIntegerField(blank=True, null=True)
    days = models.DateTimeField()


class Feedback(BaseModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField(blank=True, null=True)
    vote = models.IntegerField(default=1, validators=[MaxValueValidator(5),
                               MinValueValidator(1)])