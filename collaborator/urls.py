from django.urls import path

from collaborator import views

urlpatterns = [
    path('', views.colaborator, name="collaborator"),
]
