from . import views
from django.urls import path


urlpatterns = [
    path('datq' , views.get_api_view.as_view() ),
]