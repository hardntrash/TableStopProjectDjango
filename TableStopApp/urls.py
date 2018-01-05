from django.conf.urls import url

from . import views

app_name = 'TableStopApp'
urlpatterns = [
    url(r'^$', views.Table_Stops.as_view(), name='stops'),
]