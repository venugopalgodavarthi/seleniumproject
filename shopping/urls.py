from django.urls import path
from shopping import views
urlpatterns = [
    path('sample/', views.sample, name="sample")
]
