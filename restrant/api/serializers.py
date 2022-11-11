from rest_framework import serializers
from ..models import MainMenu, DailyMenu, Feedback


class MainMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenu
        fields = "__all__"

class DailyMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

class DailyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = "__all__"