from rest_framework import serializers
from ..models import User, Employee
from django.contrib.auth.hashers import make_password
from restrant.models import Restraunt



class RestrantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restraunt
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    restraunt_data = RestrantCreateSerializer()

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        res_data = validated_data.pop('restraunt_data')
        user = User.objects.create(**validated_data)
        user.email = validated_data.get('email')
        user.password = make_password(validated_data.get('password'))
        user.save()
        res = Restraunt.objects.create(**res_data)
        res.owner = user
        res.save()
        return validated_data

    def update(self, instance, validated_data):
        res_data = validated_data.pop('restraunt_data')
        User.objects.filter(email=instance.email).update(**validated_data)
        instance.password = make_password(validated_data.get('password'))
        instance.save()
        Restraunt.objects.filter(owner=instance).update(**res_data)
        return instance

class EmployeeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeCreateSerializer(serializers.ModelSerializer):
    user = EmployeeUserSerializer()

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        usr = User.objects.create(**user_data)
        usr.password = make_password(user_data.get('password'))
        usr.save()
        employee = Employee.objects.create(**validated_data)
        employee.user = usr
        employee.save()
        return validated_data