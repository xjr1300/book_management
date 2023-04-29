from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Eメールを設定してください。")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("スーパーユーザーは`is_staff`を`True`に設定してください。")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("スーパーユーザーは`is_superuser`を`True`に設定してください。")
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザーモデル

    下記フィールドは、AbstractBaseUserで実装されている。
    - password
    - last_login
    下記フィールドはPermissionMixinで実装されている。
    - is_superuser
    - groups
    - user_permissions
    """

    email = models.EmailField("Eメールアドレス", primary_key=True, max_length=255)
    name = models.CharField("名前", max_length=80)
    is_active = models.BooleanField("アクティブ", default=True)
    is_staff = models.BooleanField("スタッフ", default=False)
    date_joined = models.DateTimeField("登録日時", default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ("name",)

    class Meta:
        db_table = "users"
        verbose_name = verbose_name_plural = "ユーザー"
        ordering = ("email",)

    def __str__(self) -> str:
        """名前を返却する。

        Returns:
            名前
        """
        return self.name

    @property
    def username(self) -> str:
        """ユーザー名(メールアドレス)を返却する。

        Returns:
            ユーザー名(メールアドレス)。
        """
        return self.email
