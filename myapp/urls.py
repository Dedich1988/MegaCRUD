from django.urls import path
from .views import myapp_index

app_name = 'myapp'

urlpatterns = [
    path("", myapp_index, name="index"),




]


