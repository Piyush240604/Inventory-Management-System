from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser with only a username and password'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting superuser creation...'))

        username = 'admin'  # Username you want to set
        password = 'password123'  # Password you want to set

        # Check if the user already exists
        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS('Creating superuser...'))
            # Create the superuser
            user = User.objects.create_superuser(username=username, password=password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser with username: {username}'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

        self.stdout.write(self.style.SUCCESS('Superuser creation process finished.'))
