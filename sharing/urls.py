from django.conf.urls import url, patterns
import views

urlpatterns = patterns(
    '',
    url(r'^/(?P<event_id>\d+)/', views.IndexView.as_view(), name="index"),
)
