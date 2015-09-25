"""coffeedapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
	url(r'landing/$', coreviews.LandingView.as_view()),
	url(r'location/$', coreviews.LocationListView.as_view()),
    url(r'search/$', coreviews.SearchListView.as_view()),
	url(r'location/(?P<pk>\d+)/detail$', coreviews.LocationDetailView.as_view(), name='location_detail'),
    url(r'location/create/$', login_required(coreviews.LocationCreateView.as_view())),
    url(r'location/(?P<pk>\d+)/update/$', login_required(coreviews.LocationUpdateView.as_view()), name='location_update'),
    url(r'location/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name='review_create'),
    url(r'location/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name='review_update'),
    url(r'entrance/$', coreviews.entrance),
)
