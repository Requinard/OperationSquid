from django.conf.urls import url, patterns

import views
urlpatterns = patterns(
    '',
    url(r'^(?P<event_id>\d+)/create/appointment/', views.AppointmentView.as_view(), name="createAppointment"),
    url(r'^(?P<event_id>\d+)/create/news/', views.NewsView.as_view(), name="createNews"),
    url(r'^(?P<event_id>\d+)/', views.IndexView.as_view(), name="index"),
    url(r'^', views.AllView.as_view(), name="index_general"),

)

