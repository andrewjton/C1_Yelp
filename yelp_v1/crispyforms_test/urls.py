from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^standard_django/', views.first, name="first"),
	url(r'^crispy_style/', views.second, name="second"),

]