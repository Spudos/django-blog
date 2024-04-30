from django.urls import path
from about import views as about_views

urlpatterns = [
    path("about/", about_views.about, name='about'),
]