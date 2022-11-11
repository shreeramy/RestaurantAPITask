from django.contrib import admin
from .models import Restraunt, DailyMenu, MainMenu, Feedback

admin.site.register(Restraunt)
admin.site.register(DailyMenu)
admin.site.register(MainMenu)
admin.site.register(Feedback)