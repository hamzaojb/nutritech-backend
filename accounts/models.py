from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, fullname, gender, password=None):
        if not email:
            raise ValueError('L\'email est requis')
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, gender, password=None):
        user = self.create_user(email, fullname, gender, password)
        user.is_admin = True
        user.is_staff = True  # Ensure is_staff is set to True for superuser
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)  # Add the is_staff field here

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname', 'gender']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='produits/',max_length=1024, null=True, blank=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom