from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from {{ project_name }}.apps.core.views import HomeView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home_page'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )


if settings.IS_TESTING:
    urlpatterns += patterns('',
        url(r'^user/(?P<username>[\w@\.+-]+)/$', 'helpers42cc.views.profile',
            name='profile')
    )