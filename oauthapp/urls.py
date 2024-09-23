from django.urls import path, include

urlpatterns = [
    # Другие URL-адреса
    path('accounts/', include('oauthapp.urls'))
]
