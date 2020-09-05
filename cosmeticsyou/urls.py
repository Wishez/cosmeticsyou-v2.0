from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from myadmin.admin import admin_site
# import notifications.urls

urlpatterns = [
	url(r'', include('pages.urls')),
    url(r'^api/', include('home.urls')),
    url(r'^personal_room/', include('accounts.urls')),
    url(r'^registration/', include('accounts.urls')),
    url(r'^share/', include('shares.urls')),
    url(r'^shares/', include('shares.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin_site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


