from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
# from hr.models import Employer, Employee
from hr.models import Sala, Orar, Profesor, Materie, Zi, An, Grupa

AuthUserModel = get_user_model()


def get_superuser_permissions():
    generic_permissions = {"view", "add", "change", "delete"}
    model_names = {Sala.__name__.lower(), Orar.__name__.lower(), Profesor.__name__.lower(), Materie.__name__.lower(),
                   Zi.__name__.lower(), An.__name__.lower(), Grupa.__name__.lower()}
    permissions = set()

    for model_name in model_names:
        for generic_permission in generic_permissions:
            permissions.add(f"{generic_permission}_{model_name}")

    return permissions


def get_staff_permissions():
    generic_permissions = {"view"}
    model_names = {Sala.__name__.lower(), Orar.__name__.lower(), Profesor.__name__.lower(), Materie.__name__.lower(),
                   Zi.__name__.lower(), An.__name__.lower(), Grupa.__name__.lower()}
    permissions = set()

    for model_name in model_names:
        for generic_permission in generic_permissions:
            permissions.add(f"{generic_permission}_{model_name}")

    return permissions


class Command(BaseCommand):
    help = "Give all staff users the permissions to Employer and Employee models"

    def handle(self, *args, **options):
        try:
            profesor_director_permissions = get_superuser_permissions()
            db_permissions = Permission.objects.filter(codename__in=profesor_director_permissions)
            superuser_staff_permission = AuthUserModel.objects.filter(is_superuser=True, is_staff=True).all()
            for user in superuser_staff_permission:
                for db_permission in db_permissions:
                    user.user_permissions.add(db_permission)

            profesor_permissions = get_staff_permissions()
            db_permissions = Permission.objects.filter(codename__in=profesor_permissions)
            staff_permission = AuthUserModel.objects.filter(is_superuser=False, is_staff=True).all()
            for user in staff_permission:
                for db_permission in db_permissions:
                    user.user_permissions.add(db_permission)
        except BaseException as e:
            raise CommandError(e)
