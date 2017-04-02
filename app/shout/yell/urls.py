from django.conf.urls import url
from yell import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^results/$', views.restaurants, name='restaurants'),
    url(r'^api/yelp_api/$', views.yelp_api, name="yelp_api"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)