from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError("이메일 주소가 있어야 함")
        if not nickname:
            raise ValueError("닉네임이 있어야 함")

        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            password = self.make_random_password(),
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email= self.normalize_email(email),
            nickname= nickname,
            password= password
        )
        user.is_admin = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=50)
    picture = models.ImageField
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname',]