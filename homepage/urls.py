from django.urls import path
from .views import Homepageview,AboutPageViews


urlpatterns=[
    path('',Homepageview.as_view(),name="home"),
    path('about/',AboutPageViews.as_view(),name="about")
]