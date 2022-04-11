from django.core.management.base import BaseCommand
from tutorials.models import Tutorial
from user.models import User


class Command(BaseCommand):
    # Tutorial table initialized with dummy data
    def handle(instance, *args, **options):
        try:
            Tutorial.objects.get()
        except Tutorial.DoesNotExist:
            user_id = User.objects.get(pk=1).id
            title = 'Title 1'
            description = 'Description 1'
            booked = True
            tutorial = Tutorial(title=title,
                                description=description,
                                booked=booked, user_id=user_id)
            tutorial.save()
