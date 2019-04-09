from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email , password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        user = self.create_user(email,password=password)
        user.is_admin= True
        #user.is_staff = True
        user.save(using=self._db)
        return user

class Myuser(AbstractBaseUser):
    firstname = models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    email = models.EmailField(max_length=250, unique=True)
    date_of_birth = models.DateField(null=True)
    date_joined = models.DateField(null=True)
    last_login = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)
    #country_of_residence = CharField(max_length=50)
    city = models.CharField(max_length=50)
    is_watcher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff =  models.BooleanField(default=True)
    objects  = MyUserManager()


    USERNAME_FIELD = 'email'
    EMAILFIELD = 'email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, registration_app):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
