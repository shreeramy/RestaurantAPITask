from rest_framework import serializers
from ..models import MainMenu, DailyMenu, Feedback, Restraunt


class MainMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainMenu
        fields = "__all__"

class DailyMenuCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = "__all__"

class RestrauntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restraunt
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    restraunt = serializers.SerializerMethodField()
    class Meta:
        model = Feedback
        fields = ['restraunt']
    
    def get_restraunt(self, instance):
        data = Restraunt.objects.filter(id=instance).first()
        serializer = RestrauntSerializer(data)
        return serializer.data

class DailyMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyMenu
        fields = "__all__"
