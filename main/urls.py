from main import views
from django.urls import path

urlpatterns = [
    path('mail/',views.send_email),
    path('custom_email/',views.customEmail),
]