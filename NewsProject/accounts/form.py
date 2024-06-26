from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        print(common_users)
        user.groups.add(common_users)
        return user
