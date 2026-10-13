from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<str:name>/", views.hello, name="hello"),
    path("api/status/", views.api_status, name="api_status"),
    path("about/", views.about, name="about"),
    path("api/add/<int:a>/<int:b>/", views.add, name="add"),
]