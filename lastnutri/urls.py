# lastnutri/urls.py

from django.contrib import admin
from django.urls import path, include  # <-- Add this import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Ensure this is correctly linked to your app's URLs

]
