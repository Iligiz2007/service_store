from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('appss.user.urls')),
    path('',include("appss.shop.urls")),
    path('chat/',include('appss.chat.urls')),

    
    path('api/shop/', include('appss.shop.api_urls')),
    path('api/user/',include('appss.user.api_urls')),
    path('api/chat/',include('appss.chat.api_urls')),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
