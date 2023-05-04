from .models import User
from django.contrib.auth.backends import BaseBackend
from django.urls import reverse


class LoginBackend(BaseBackend):
    def authenticate(self, request, username, password, **kwargs):
        try:
            user = User.objects.get(cc=username)
            pass_check = user.check_password(password)

            print(f"Pass:{pass_check}")

            if pass_check:
                print("Si tienen la misma pass")
                return user
        except User.DoesNotExist:
            return None

    def get_success_url():
        return reverse("app_projects:home")

    def login_success(self):
        from django.shortcuts import redirect

        return redirect(self.get_success_url())
