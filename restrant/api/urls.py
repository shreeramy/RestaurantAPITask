from django.urls import path
from .api_views import (
    MainMenuCreateView, 
    MainMenuView, 
    DailyMenuCreateView, 
    DailyMenuView, 
    FeedbackView)

urlpatterns = [
    path("main_menu_create/", MainMenuCreateView.as_view()),
    path("main_menu/", MainMenuView.as_view()),
    path("daily_menu_create/",DailyMenuCreateView.as_view()),
    path("daily_menu/",DailyMenuView.as_view()),
    path("feedback/",FeedbackView.as_view())
]
