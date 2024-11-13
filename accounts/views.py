from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from accounts.models import User  # Utiliser le modèle personnalisé User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
import json
# Importation du modèle Produit
from accounts.models import Produit


# Inscription d'un nouvel utilisateur
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            fullname = data.get('fullname')
            gender = data.get('gender')
            password = data.get('password')

            # Vérifier si l'email existe déjà
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message': 'Cet email est déjà utilisé.'}, status=400)

            # Créer un nouvel utilisateur
            user = User.objects.create_user(email=email, fullname=fullname, gender=gender, password=password)

            return JsonResponse({'message': 'Inscription réussie !'}, status=201)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)

# Connexion d'un utilisateur
@csrf_exempt
def signin(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Authentifier l'utilisateur avec l'email comme username
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Connexion réussie !'}, status=200)
            else:
                return JsonResponse({'message': 'Identifiants incorrects'}, status=400)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)

# Liste des utilisateurs
@csrf_exempt
def list_users(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()  # Récupérer tous les utilisateurs
            user_data = [
                {
                    'id': user.id,  # Ajout de l'ID pour modifier ou supprimer
                    'email': user.email,
                    'fullname': user.fullname,
                    'gender': user.gender,
                    'is_active': user.is_active,
                    'is_admin': user.is_admin
                }
                for user in users
            ]
            return JsonResponse({'users': user_data}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)

# Modifier un utilisateur
@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            user = User.objects.get(id=user_id)  # Récupérer l'utilisateur par ID

            # Mise à jour des champs de l'utilisateur
            user.email = data.get('email', user.email)
            user.fullname = data.get('fullname', user.fullname)
            user.gender = data.get('gender', user.gender)
            if 'password' in data:
                user.set_password(data['password'])  # Sécuriser le mot de passe
            user.save()  # Sauvegarder les modifications

            return JsonResponse({'message': 'Utilisateur mis à jour avec succès !'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)

# Supprimer un utilisateur
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=user_id)  # Récupérer l'utilisateur par ID
            user.delete()  # Supprimer l'utilisateur

            return JsonResponse({'message': 'Utilisateur supprimé avec succès !'}, status=200)

        except User.DoesNotExist:
            return JsonResponse({'message': 'Utilisateur non trouvé'}, status=404)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)
@csrf_exempt
def add_produit(request):
    if request.method == 'POST':
        try:
            nom = request.POST.get('nom')
            prix = request.POST.get('prix')
            image = request.FILES.get('image')  # Gestion du fichier image

            if not nom or not prix or not image:
                return JsonResponse({'message': 'Nom, prix et image sont obligatoires'}, status=400)

            produit = Produit.objects.create(nom=nom, prix=prix, image=image)

            return JsonResponse({'message': 'Produit ajouté avec succès!', 'produit': {
                'id': produit.id,
                'nom': produit.nom,
                'prix': str(produit.prix),
                'image_url': produit.image.url if produit.image else None
            }}, status=201)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)

@csrf_exempt
def list_produits(request):
    if request.method == 'GET':
        try:
            produits = Produit.objects.all()  # Récupérer tous les produits
            produit_data = [
                {
                    'id': produit.id,
                    'nom': produit.nom,
                    'image_url': produit.image.url if produit.image else None,
                    'prix': str(produit.prix)  # Convertir en string si nécessaire pour JSON
                }
                for produit in produits
            ]
            return JsonResponse({'produits': produit_data}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Méthode non autorisée'}, status=405)