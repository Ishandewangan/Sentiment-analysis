from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name="homePage"),
    path('inputFromUser',views.inputFromUser,name="inputFromUser"),
    path("history",views.history,name="history"),
    path('result/<str:text>/',views.sentimentAnalysisResult,name='sentimentAnalysisResult'),
]
