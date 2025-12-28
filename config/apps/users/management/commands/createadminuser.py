from apps.users.models.admin import AdminUser
from apps.users.models.user import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create an admin user with the given email and password."

    def add_arguments(self, parser):
        parser.add_argument(
            "--email",
            type=str,
            required=True,
            help="Email address for the admin user.",
        )
        parser.add_argument(
            "--password",
            type=str,
            required=True,
            help="Password for the admin user.",
        )

    def handle(self, *args, **options):
        email = options["email"]
        password = options["password"]

        user, created = User.objects.get_or_create(
            email=email, defaults={"password": password}
        )
        if created:
            user.set_password(password)
            user.save()

        _, admin_created = AdminUser.objects.get_or_create(user=user)

        if created and admin_created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin user with email {email} created successfully."
                )
            )
        elif admin_created:
            self.stdout.write(
                self.style.SUCCESS(f"Existing user {email} promoted to admin.")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Admin user with email {email} already exists.")
            )
