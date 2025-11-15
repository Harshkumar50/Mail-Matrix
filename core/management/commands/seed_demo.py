from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Mail


class Command(BaseCommand):
    help = "Seed demo users and mails"

    def handle(self, *args, **options):
        demo1, _ = User.objects.get_or_create(username="demo1", defaults={"email": "demo1@example.com"})
        if not demo1.has_usable_password():
            demo1.set_password("demo1234")
            demo1.save()
        demo2, _ = User.objects.get_or_create(username="demo2", defaults={"email": "demo2@example.com"})
        if not demo2.has_usable_password():
            demo2.set_password("demo1234")
            demo2.save()

        if not Mail.objects.exists():
            Mail.objects.create(sender=demo1, receiver=demo2, subject="Hello from demo1", body="Hi demo2! Welcome to Mail Dashboard.")
            Mail.objects.create(sender=demo2, receiver=demo1, subject="Re: Hello", body="Thanks demo1! Looks great.")
            Mail.objects.create(sender=demo1, receiver=demo2, subject="Project Update", body="We are on track for the release.")
            Mail.objects.create(sender=demo2, receiver=demo1, subject="Meeting Reminder", body="Reminder: Sync at 3 PM UTC.")

        self.stdout.write(self.style.SUCCESS("Demo users and mails seeded."))




