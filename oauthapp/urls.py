from django.urls import path, include


urlpatterns = [
    # Другие URL-адреса
    path('oauth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('oauthapp.urls'))
]