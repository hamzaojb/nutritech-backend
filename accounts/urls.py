from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('users/', views.list_users, name='list_users'),  # Nouvelle URL pour lister les utilisateurs
     path('users/<int:user_id>/update/', views.update_user, name='update_user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    # Ajouter les routes pour les produits
    path('produits/', views.list_produits, name='list_produits'),
    path('produits/add/', views.add_produit, name='add_produit'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)