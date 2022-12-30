from django.urls import path

from basic_app import views

urlpatterns = [
    path('user/', views.ListUser.as_view()),
    path('user/<int:pk>', views.DeatilUser.as_view())
]
