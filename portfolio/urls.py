from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/mobile", views.mobile, name="mobile"),
    path("portfolio/apps", views.apps, name="apps"),
    path("portfolio/sites", views.sites, name="sites"),
    path("portfolio/graphic", views.graphic, name="graphic"),
    path("blog", views.blog, name="blog"),
    path("contact", views.contact, name="contact"),
    path("error", views.error, name="error")
]
