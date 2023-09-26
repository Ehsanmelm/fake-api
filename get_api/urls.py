from . import views
from django.urls import path


urlpatterns = [
    path('data/' , views.GetDataView.as_view() ),
]