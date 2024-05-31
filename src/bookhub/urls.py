from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

doc_urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bookhub.apps.books.urls')),
    path('api/authors/', include('bookhub.apps.authors.urls')),
    path('api/translators/', include('bookhub.apps.translators.urls')),
    path('api/publishers/', include('bookhub.apps.publishers.urls')),
    path('api/login/', views.obtain_auth_token),
    path('api/register/', include('bookhub.auths.users.urls')),
]+doc_urlpatterns
