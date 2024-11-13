# lastnutri/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Add this import statement
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Ensure this is correctly linked to your app's URLs

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)