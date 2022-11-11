from django.urls import path
from .api_views import (
    MainMenuCreateView, 
    MainMenuView, 
    DailyMenuCreateView, 
    DailyMenuView, 
    FeedbackView,
    FeedbackListView,
    TopMenuListView)

urlpatterns = [
    path("main_menu_create/", MainMenuCreateView.as_view()),
    path("main_menu/", MainMenuView.as_view()),
    path("daily_menu_create/", DailyMenuCreateView.as_view()),
    path("daily_menu/", DailyMenuView.as_view()),
    path("feedback/", FeedbackView.as_view()),
    path("feedback_list/", FeedbackListView.as_view()),
    path("top_daily_menu/", TopMenuListView.as_view()),
]
