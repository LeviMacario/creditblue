from django.contrib.auth.models import UserManager as BaseUserManager
from core.managers import InRangeMixin
from datetime import date


class UserManager(BaseUserManager, InRangeMixin):
    def logged_this_month(self):
        today = date.today()
        return self.in_range(
            'last_login',
            today, today.replace(day=1))
