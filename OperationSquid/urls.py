from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns(
    '',
    # Examples:
    # url(r'^$', 'OperationSquid.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/', include("user_account.urls", namespace="user")),
    url(r'^external/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^live/', include('sharing.urls', namespace='live')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^overseer/', include('overseer.urls', namespace="overseer")),
    url(r'^', include("events.urls", namespace="events")),
)
