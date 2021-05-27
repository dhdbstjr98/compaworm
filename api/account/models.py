from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(
        self, sns_id, name, profile="./img/profile_no_image.png", password=None
    ):
        if not id or not name or not profile:
            raise ValueError("Users must have id, name, profile")

        user = self.model(sns_id=sns_id, name=name, profile=profile)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, sns_id, name, password, profile="./img/profile_no_image.png"
    ):
        user = self.create_user(
            sns_id=sns_id, name=name, profile=profile, password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    sns_id = models.CharField(max_length=200, unique=True, null=False)
    name = models.CharField(max_length=200, null=False)
    profile = models.CharField(max_length=200, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "sns_id"
    REQUIRED_FIELDS = ["name", "profile"]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class UserToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=36)
    expires = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=1))
