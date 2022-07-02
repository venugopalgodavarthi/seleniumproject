from django.urls import path
from online import views
urlpatterns = [
    path('university/', views.universityview, name="university"),
    path('college/', views.collegeview, name="college"),

    path('universitys/', views.universityviewselect, name="universitys"),
    path('colleges/', views.collegeviewselect, name="colleges"),

    path('universityu/<pk>/', views.universityviewupdate, name="universityu"),
    path('collegeu/<pk>/', views.collegeviewupdate, name="collegeu"),

    path('universityd/<pk>/', views.universityviewdelete, name="universityd"),
    path('colleged/<pk>/', views.collegeviewdelete, name="colleged"),

]
