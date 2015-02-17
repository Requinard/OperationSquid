from django.conf.urls import url, patterns

import views

urlpatterns = patterns(
    '',
    url(r'^event/(?P<event_id>\d+)/', views.EventView.as_view(), name="event"),
    url(r'^', views.IndexView.as_view(), name="index"),
)

