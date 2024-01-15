from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, nickname, name, phone_num, child_name, child_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not name:
            raise ValueError('must have user name')
        if not phone_num:
            raise ValueError('must have user phone_num')
        if not child_name:
            raise ValueError('must have user child_name')
        if not child_birth:
            raise ValueError('must have user child_birth')

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            name=name,
            phone_num=phone_num,
            child_name=child_name,
            child_birth=child_birth,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, phone_num, child_name, child_birth, password=None, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            nickname=nickname,
            name=name,
            phone_num=phone_num,
            child_name=child_name,
            child_birth=child_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    phone_num = models.CharField(default='', max_length=20, null=False, blank=False)
    child_name = models.CharField(default='', max_length=100, null=False, blank=False)
    child_birth = models.DateField(null=False, blank=False)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name', 'phone_num', 'child_name', 'child_birth']

    def __str__(self):
        return self.nickname
