from django.urls import path

from .views import AboutView, HomeView, ContactView

urlpatterns = [
    path("", HomeView.as_view()),
    path("about/", AboutView.as_view()),
    path("contact/", ContactView.as_view()),
]
