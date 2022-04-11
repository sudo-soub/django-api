from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    # This command is for creating and initial user for the app
    def handle(self, *args, **options):
        try:
            User.objects.get()
        except User.DoesNotExist:
            username = 'test'
            password = 'test@123'
            new_user = User(username=username, password=password)
            new_user.save()
            print('Initial user created with following credentials:')
            print('username:', username)
            print('password:', password)
