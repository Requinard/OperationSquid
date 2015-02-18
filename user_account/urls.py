from django.conf.urls import url, patterns

import views

urlpatterns = patterns(
    '',
    url(r'^login/', views.LoginView.as_view(), name="login"),
    url(r'^logout/', views.LogoutView.as_view(), name="logout"),

)
