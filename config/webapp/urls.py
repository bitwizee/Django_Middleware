from django.urls import path
from .views import activity_log_view


urlpatterns = [
    path('activity/', activity_log_view)
]
