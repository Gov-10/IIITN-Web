from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
   path("", views.home, name="home"),
   path("about", views.about, name="about"),
   path("governance", views.governance, name="governance"),
   path("department", views.department, name="department"),
   path("alumni", views.alumni, name="alumni"),
   path("placements", views.placements, name="placements"),
   path("nirf", views.nirf, name="nirf"),
    path("off_docs", views.off_docs, name="off_docs"),
    path("committee", views.committee, name="committee"),
    path("administration", views.administration, name="administration"),
    path("ece", views.ece, name="ece"),
    path("cse", views.cse, name="cse"),
    path("bsc", views.bsc, name="bsc"),
    path("docs", views.docs, name="docs"),
    path("progs", views.progs, name="progs")


]