from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from accounts.models import User  # Utiliser le modèle personnalisé User
from django.views.decorators.csrf import csrf_exempt
import json

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
