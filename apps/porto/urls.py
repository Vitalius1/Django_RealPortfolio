from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^testimonials$', views.showTestimonials),
    url(r'^projects$', views.showProjects),
    url(r'^about$', views.showAbout)
]