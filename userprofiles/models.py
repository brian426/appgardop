from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserprofileManager(BaseUserManager):
    def create_user(self, email, name,lastname,nroDocument,documentType, password=None):
        """
        Creates and saves a User with the given email,name 
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            lastname=lastname,
            nroDocument=nroDocument,
            documentType=documentType,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,lastname,nroDocument,documentType, password):
        """
        Creates and saves a superuser with the given email, name
        and password.
        """
        user = self.create_user(email,
            password=password,
            name=name,
            lastname=lastname,
            nroDocument=nroDocument,
            documentType=documentType,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Userprofile(AbstractBaseUser):
	IDENTITY_DOCUMENT = (
		('DNI', 'Dni'),
		('PAS', 'Pasaporte'),
	)
	email = models.EmailField(
	    verbose_name='email address',
	    max_length=255,
	    unique=True,
	)
	name = models.CharField(max_length=255)
	lastname = models.CharField(max_length=255)
	documentType= models.CharField(max_length=3,
		verbose_name='tipo de documento',
		choices=IDENTITY_DOCUMENT)
	nroDocument = models.IntegerField(verbose_name='Numero de documento',unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = UserprofileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name','lastname','nroDocument','documentType',]

	def get_full_name(self):
	    # The user is identified by their email address
	    return self.email

	def get_short_name(self):
	    # The user is identified by their email address
	    return self.email

	def __str__(self):              # __unicode__ on Python 2
	    return '%s' % (self.name+" "+self.lastname) 

	def has_perm(self, perm, obj=None):
	    "Does the user have a specific permission?"
	    # Simplest possible answer: Yes, always
	    return True

	def has_module_perms(self, app_label):
	    "Does the user have permissions to view the app `app_label`?"
	    # Simplest possible answer: Yes, always
	    return True

	@property
	def is_staff(self):
	    "Is the user a member of staff?"
	    # Simplest possible answer: All admins are staff
	    return self.is_admin