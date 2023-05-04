from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def create_user(self, user_cc, password=None, role=None, **extra_fields):
        if not user_cc:
            raise ValueError("La cédula es obligatoria")
        user_cc = self.normalize_email(user_cc)
        user = self.model(user_cc=user_cc, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        if role:
            UserRole.objects.create(user=user, role=Role.objects.get(pk=role))

        return user

    def create_superuser(self, user_cc, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(user_cc, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    user_cc = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to="fotos", blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "user_cc"
    REQUIRED_FIELDS = ["full_name", "email", "phone", "birth_date"]

    objects = UserManager()

    def __str__(self):
        return self.full_name


class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.id_role} - Name:  {self.name}"


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str___(self):
        return f"{self.user} - Rol:  {self.role}"
