import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# account for superuser model

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
           raise ValueError('user must have an email')

        if not username:
           raise ValueError('user must have username')

        user = self.model(
            email = self.normalize_email(email),#this normalize will get any case of the letter the user input and turn it to lowercase
            username = username,
            first_name = first_name,
            last_name = last_name,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name,username,email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password= password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin =True
        user.save(using= self._db)
        return user



# here i create my own user account model

class account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50, blank=True)

    #because this is a custom user model , the part below are required

    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)

    #changing the login from username to email and setting up the required fields

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name', 'last_name', ] 

    object = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

# NOTe: after creating the custom user model, i need to go back to the settings.py to tell django 
# i am using a custon user model. 
#FORMAT: in settings.py , right under the WSGI, write this code below
# AUTH_USER_MODEL = 'account.account' 
# that is the model app.model name 

# and before we migrate this new user model to the database, we need to delete the old database,
# so that there will be no mixed up, also remember to register your models any time we create a new 
# model


# Here i want to create my user profile model 

class Profile(models.Model):
    user = models.OneToOneField(account, on_delete=(models.CASCADE))
    id_user = models.IntegerField()
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to= 'profile_images', default='default_profile_image.jpg')
    date_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=50, blank=True)
    work_place = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username




