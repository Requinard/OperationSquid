from django.conf.urls import url, patterns

import views


urlpatterns = patterns(
    '',
    url(r'^(?P<event_id>\d+)/message/(?P<message_id>\d+)/', views.MessageView.as_view(), name="message"),
    url(r'^(?P<event_id>\d+)/message/new/', views.NewMessageView.as_view(), name="new_message"),
    url(r'^(?P<event_id>\d+)/', views.IndexView.as_view(), name="index"),
)
