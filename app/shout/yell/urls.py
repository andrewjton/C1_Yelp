from django.conf.urls import url
from testing_ajax import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
	url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^$', views.transaction, name='transaction'),
    url(r'^success/$', views.success, name='success'),
    url(r'^restaurants/$', views.restaurants, name='restaurants'),
    url(r'^results/$', views.ajax_template, name='ajax_template'),
    url(r'^api/yelp_api/$', views.yelp_api, name="yelp_api"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)