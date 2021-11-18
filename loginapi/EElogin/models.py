from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser 
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# import AuthUser
from .managers import CustomUserManager

# Create your models here.
# class User(AbstractBaseUser, PermissionsMixin):
ADMIN = 1
TECHNICIAN = 2
EMPLOYEE = 3

ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (TECHNICIAN, 'TECHNICIAN'),
    (EMPLOYEE, 'Employee')
)

class Meta:
    verbose_name = 'user'
    verbose_name_plural = 'users'

    # These fields tie to the roles!
#punia123    punia@gmail.com
class User(AbstractBaseUser, PermissionsMixin):

  # Roles created here
        uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=30, blank=True)
        last_name = models.CharField(max_length=50, blank=True)
        is_staff = models.BooleanField(_('staff status'), default=False)
        is_active = models.BooleanField(_('active'), default=True)
        role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
        date_joined = models.DateTimeField(auto_now_add=True)
        is_active = models.BooleanField(default=True)
        is_deleted = models.BooleanField(default=False)
        created_date = models.DateTimeField(default=timezone.now)
        modified_date = models.DateTimeField(default=timezone.now)
        created_by = models.EmailField()
        modified_by = models.EmailField()

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []

        objects = CustomUserManager()

        def __str__(self):
            return self.email
        class Meta:
            """
            Model name in database
            """
            verbose_name = _('user')
            verbose_name_plural = _('users')
            ordering = ['date_joined', ]
            db_table = 'user'

        def get_full_name(self):
            """
            return: full name of user
            """
            full_name = '{} {}'.format(self.first_name, self.last_name)
            return full_name.strip()

        def get_short_name(self):
            """
            return short or nick name of user
            """
            return self.first_name


