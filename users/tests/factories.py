import factory
from users.models import User
from django.contrib.auth.hashers import make_password
from factory import LazyAttribute
from factory.django import DjangoModelFactory
from faker import Factory


faker = Factory.create()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = LazyAttribute(lambda o: faker.name())
    last_name = LazyAttribute(lambda o: faker.name())
    email = LazyAttribute(lambda o: faker.email())
    password = factory.LazyFunction(lambda: make_password("testpassword.123"))
    is_staff = False
    is_superuser = False